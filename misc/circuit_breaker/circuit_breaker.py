#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from collections import deque

import flask
from flask import Flask
import requests


app = Flask(__name__)

SERVER = None
BAD_CODES = [500]
CODES = deque()
CB_ERROR_RATIO_THRESHOLD = None
SLIDING_WINDOW_LEN = 10


@app.route('/')
def cb_handler():
    global CODES
    error_ratio = count_error_ratio(CODES)
    if len(CODES) >= SLIDING_WINDOW_LEN and error_ratio >= CB_ERROR_RATIO_THRESHOLD:
        cb_response_content = 'Service is down! Error ratio: {} (threshold: {})'.format(
            error_ratio,
            CB_ERROR_RATIO_THRESHOLD,
        )
        cb_status_code = 200
        cb_response = flask.Response(
            response=cb_response_content,
            status=cb_status_code,
        )
    else:
        service_path = '/'
        service_response = requests.get(
            '{srv}{p}'.format(srv=SERVER, p=service_path)
        )
        service_status_code = service_response.status_code

        upd_error_ratio(CODES, service_status_code, SLIDING_WINDOW_LEN)

        cb_response = flask.Response(
            response=service_response.content,
            status=service_status_code,
        )

    return cb_response


def upd_error_ratio(codes, status_code, window_len=10):
    if len(codes) >= window_len:
        codes.pop()
    codes.appendleft(int(status_code))


def count_error_ratio(codes):
    if not codes:
        return 0.0
    global BAD_CODES
    curr_avg = len([error for error in codes if error in BAD_CODES]) / len(codes)
    print('Current error ratio: {}'.format(curr_avg))
    return curr_avg


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--server', type=str, default='http://localhost:8080')
    parser.add_argument('--error-ratio-threshold', type=float, default=0.4)
    return parser.parse_args()


def main():
    args = get_args()

    global SERVER
    SERVER = args.server
    global CB_ERROR_RATIO_THRESHOLD
    CB_ERROR_RATIO_THRESHOLD = args.error_ratio_threshold

    app.run(port=args.port)


if __name__ == "__main__":
    main()
