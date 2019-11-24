#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import requests
import flask
from flask import Flask
import json
import itertools

app = Flask(__name__)

SERVERS_POOL = None


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def balancer_handler(path):
    # FIXME
    # circuit breaker
    current_server = next(SERVERS_POOL)
    print('Current server: ', current_server)
    service_response = requests.get(
        '{srv}{hndl}'.format(srv=current_server, hndl='/')
    )
    balancer_response = flask.Response(
        service_response.content,
        status=service_response.status_code,
    )

    return balancer_response


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int)
    parser.add_argument('--servers', type=str)
    args = parser.parse_args()
    return args


def parse_servers(servers_str):
    global SERVERS_POOL
    servers_list = json.loads(servers_str)
    SERVERS_POOL = itertools.cycle(servers_list)


def main():
    args = get_args()
    parse_servers(args.servers)
    app.run(port=args.port)


if __name__ == '__main__':
    main()
