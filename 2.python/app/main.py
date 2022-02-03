#!/usr/bin/env python3.9

from flask import Flask, render_template, request, make_response
from guestbook import GuestBook

# global constants
PSQL_DB_NAME: str = 'guest_book'
PSQL_DB_USER: str = 'user'
PSQL_DB_HOST: str = 'host.docker.internal'
PSQL_DB_PORT: int = 5432
TABLE_NAME: str = 'guests'

# initialize global guestbook instance
GUESTS: GuestBook = GuestBook(
    db_name=PSQL_DB_NAME, 
    db_user=PSQL_DB_USER, 
    table_name=TABLE_NAME,
    db_host=PSQL_DB_HOST,
    db_port=PSQL_DB_PORT
)
GUESTS.create_table()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Return guest list.
    """
    all_guests: list = [ 
        {'id': guest[0], 'name': guest[1]}
        for guest in GUESTS.get_guest_list()
    ]
    return make_response({'guests': all_guests}, 200)


@app.route('/add', methods=['GET'])
def add():
    """
    Add a new guest.
    """
    guest_name: str = request.args.get('name')
    if not guest_name:
        return make_response("Call /add?name=NewGuestName", 400)
    else:
        guest_id: int = GUESTS.add_guest(guest_name)
        return make_response({'id': guest_id}, 200)


@app.route('/guest/<gid>', methods=['GET', 'DELETE'])
def guest(gid):
    """
    Rename or delete an existing guest.
    """
    # path to rename guest
    if request.method == 'GET':
        guest_name: str = request.args.get('name')
        if not guest_name:
            return make_response("Call /guest/<gid>?name=NewGuestName", 400)
        else:
            GUESTS.update_guest_name_by_id(
                guest_id=gid, new_name=guest_name
            )
            return make_response({'status': 'ok'}, 200)
    # path to delete guest
    else:
        GUESTS.remove_guest_by_id(guest_id=gid)
        return make_response({'status': 'ok'}, 200)


if __name__ == '__main__':
    # run the Flask development server
    app.run(host='0.0.0.0', threaded=True, port=80, use_reloader=True)
