#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def gen_file(filename, n, min_value=-10, max_value=10, seed=12345):
    random.seed(seed)
    data = (str(random.uniform(min_value, max_value)) + '\n' for i in xrange(n))
    with open(filename, 'w') as output_file:
        output_file.writelines(data)


def get_values(filename):
    with open(filename, 'r') as input_file:
        try:
            return map(float, input_file)
        except ValueError:
            raise ValueError('File {!r} contains invalid values'.format(filename))


def get_expected_value(values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        raise ZeroDivisionError('Wrong number of values')
    except TypeError:
        raise TypeError('"Values" should be a container object')


def get_variance(values):
    if not values:
        raise ValueError('Wrong values list or expected value')
    mean = get_expected_value(values)
    variance = sum(map(lambda v: (v - mean) ** 2, values)) / len(values)
    return variance

if __name__ == '__main__':
    filename_in = 'metric.txt'
    # gen_file(fname_in, 10)
    values = get_values(filename_in)
    expected_value = get_expected_value(values)
    variance = get_variance(values)
    print 'Expected value: {exp}\nDispersion: {var}'.format(
        exp=expected_value,
        var=variance
    )
