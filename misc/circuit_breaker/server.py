#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random

import flask
from flask import Flask


app = Flask(__name__)

ERROR_PROB = None


@app.route('/')
def app_main_handler():
    if random.random() < ERROR_PROB:
        response_content = '{} ERROR\n'.format(flask.request.host)
        response_status_code = 500
    else:
        response_content = 'Hello from {}\n'.format(flask.request.host)
        response_status_code = 200

    return flask.Response(
        response=response_content,
        status=response_status_code,
    )


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--error-prob', type=float, default=0.0)
    return parser.parse_args()


def main():
    args = get_args()

    global ERROR_PROB
    ERROR_PROB = args.error_prob

    app.run(port=args.port)


if __name__ == "__main__":
    main()
