FROM tiangolo/uwsgi-nginx-flask:python3.10

LABEL maintainer="Samm Du <hmu@sammdu.com>"

# install requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app
