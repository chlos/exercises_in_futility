#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import flask
import time
import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def app_handler():
    # FIXME:
    # * sleeps / 500 flags
    # * fault injection (500 errors percentage)
    random_sleep()
    return '{} OK'.format(flask.request.host)


def random_sleep():
    time_sleep = random.randint(1, 5)
    print('Sleep for {}s...'.format(time_sleep))
    time.sleep(time_sleep)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    app.run(debug=True, port=args.port)


if __name__ == "__main__":
    main()
