#!/usr/bin/env bash
sudo docker run -dp 80:80 --network="host" --add-host=host.docker.internal:host-gateway bcr-python-app
