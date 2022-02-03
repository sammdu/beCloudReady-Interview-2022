#!/usr/bin/env python3.9

import psycopg2

class GuestBook:
    """
    A class that allows for the interaction with the guest book.

    Public methods:
        - GuestBook(db_name: str, db_user: str, table_name: str) -> None
        - GuestBook.create_table() -> None
        - GuestBook.add_guest(guest_name: str) -> int
        - GuestBook.get_guest_list() -> list[tuple]
        - GuestBook.update_guest_name_by_id(guest_id: str) -> tuple
        - GuestBook.remove_guest_by_id(guest_id: str) -> None
    """

    db_name: str
    db_user: str
    db_host: str
    db_port: int
    table_name: str

    def __init__(
        self,
        db_name: str,
        db_user: str,
        table_name: str,
        db_host: str = 'localhost',
        db_port: int = 5432
    ) -> None:
        """
        Configure class-wide variables useful for interacting with the 
        database.
        """
        self.db_name = db_name
        self.db_user = db_user
        self.db_host = db_host
        self.db_port = db_port
        self.table_name = table_name

    def _get_conn_cur(self) -> tuple[
            psycopg2.extensions.connection, 
            psycopg2.extensions.cursor
        ]:
        """
        Return database connaction and cursor objects.
        """
        conn: psycopg2.extensions.connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.db_user,
            host=self.db_host,
            port=self.db_port
        )
        cur: psycopg2.extensions.cursor = conn.cursor()

        return conn, cur

    def create_table(self) -> None:
        """
        Create a guests table in the database.
        """
        # create a connection to the database and obtain a cursor
        conn, cur = self._get_conn_cur()

        # SQL statement to create the guests table
        stmt = f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id serial PRIMARY KEY,
                name varchar
            );
        '''

        # attempt to execute the SQL statement
        cur.execute(stmt)
        conn.commit()

        # close the database connection
        conn.close()

    def add_guest(self, guest_name: str) -> int:
        """
        Add a new guest in the guest list. 
        Return the guest ID as an integer.
        """
        # create a connection to the database and obtain a cursor
        conn, cur = self._get_conn_cur()

        # SQL statement to add a new guest to the guests table
        stmt = f'''
            INSERT INTO {self.table_name} (name) VALUES (%(name)s)
            RETURNING id;
        '''

        # attempt to execute the SQL statement and fetch the new 
        # guest ID
        cur.execute(stmt, {'name': guest_name})
        conn.commit()
        guest_id: int = cur.fetchone()[0]

        # close the database connection
        conn.close()

        return guest_id

    def get_guest_list(self) -> list[tuple]:
        """
        Get all guests on the guest list.
        """
        # create a connection to the database and obtain a cursor
        conn, cur = self._get_conn_cur()

        # SQL statement to fetch all products
        stmt = f'SELECT * FROM {self.table_name};'

        cur.execute(stmt)
        all_guests: list[tuple] = cur.fetchall()

        # close the database connection
        conn.close()

        return all_guests

    def update_guest_name_by_id(self, guest_id: int, new_name: str) -> None:
        """
        Change the name of a guest specified by its id.
        """
        # create a connection to the database and obtain a cursor
        conn, cur = self._get_conn_cur()

        # SQL statement to update the guest's name
        stmt = f'''
            UPDATE {self.table_name} SET name = %(new_name)s
            WHERE id = %(id)s;
        '''

        # attempt to execute the SQL statement and update guest's name
        cur.execute(stmt, {'new_name': new_name, 'id': guest_id})
        conn.commit()

        # close the database connection
        conn.close()

    def remove_guest_by_id(self, guest_id: int) -> None:
        """
        Remove a guest specified by its id.
        """
        # create a connection to the database and obtain a cursor
        conn, cur = self._get_conn_cur()

        # SQL statement to remove a guest from the guests table
        stmt = f'''
            DELETE FROM {self.table_name} WHERE id = %(id)s;
        '''

        # attempt to execute the SQL statement and remove the guest
        cur.execute(stmt, {'id': guest_id})
        conn.commit()

        # close the database connection
        conn.close()

    def remove_all_guests(self) -> None:
        """
        Remove all guests from the table.
        """
        # create a connection to the database and obtain a cursor
        conn, cur = self._get_conn_cur()

        # SQL statement to remove all guests from the guests table
        stmt_del = f'''
            DELETE FROM {self.table_name};
        '''

        # SQL statement to reset guest IDs to 1
        stmt_rst = f'''
            ALTER SEQUENCE {self.table_name}_id_seq RESTART;
        '''

        # attempt to execute the SQL statements above
        cur.execute(stmt_del)
        cur.execute(stmt_rst)
        conn.commit()

        # close the database connection
        conn.close()


if __name__ == '__main__' :
    import pprint as pp

    # connect to the database and create a table if it doesn't exist
    gb = GuestBook(
        db_name='guest_book', db_user='user', table_name='guests'
    )
    gb.create_table()

    # add some guests
    id_1 = gb.add_guest("John Doe")
    print(f'Added guest {id_1}')
    id_2 = gb.add_guest("Jane Smith")
    print(f'Added guest {id_2}')
    id_3 = gb.add_guest("Joe Jackson")
    print(f'Added guest {id_3}')

    # view the added guests
    guest_list = gb.get_guest_list()
    pp.pprint(guest_list)

    # update a guest's name
    gb.update_guest_name_by_id(guest_id=id_3, new_name="Joe Jackson Jr.")
    print(f'Renamed guest {id_3}')
    
    # view the added guests
    guest_list = gb.get_guest_list()
    pp.pprint(guest_list)

    # delete a guest
    gb.remove_guest_by_id(guest_id=id_1)
    print(f'Deleted guest {id_1}')

    # view the added guests
    guest_list = gb.get_guest_list()
    pp.pprint(guest_list)

    # clear table
    gb.remove_all_guests()
