#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import operator
import re

# Force matplotlib to not use any Xwindows backend.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats


def get_color(start=0xF44444, step=0x2C4FF, sign=-1):
    curr_color = start
    while True:
        curr_color += sign * step
        if curr_color > 0:
            yield '#{:X}'.format(curr_color)
        else:
            raise StopIteration


def get_counts_from_file(filename):
    rates_count = collections.defaultdict(int)
    with open(filename, 'r') as input_file:
        for line in input_file:
            m = re.match(r'.+RELEVANCE\=([A-Z0-9_]+)', line)
            if m:
                rate_name = m.group(1)
                rates_count[rate_name] += 1
    return rates_count


def get_distribution(rates_count):
    rates_total = sum(rates_count.values())
    rates_dist = {}
    for rate_name, count in rates_count.iteritems():
        rates_dist[rate_name] = float(count) / rates_total
    return rates_dist


def get_sample(rates_count, rate_name):
    rates_total = sum(rates_count.values())
    rates_tested = rates_count[rate_name]
    rates_other = rates_total - rates_tested
    return [1] * rates_tested + [0] * rates_other


def make_plot(rates_distribution, fname_plot='plot.png'):
    companies = rates_distribution.keys()
    # set the bar width
    bar_width = 0.55
    # positions of the left bar-boundaries
    bar_l = xrange(len(companies))
    # positions of the x-axis ticks (center of the bars as bar labels)
    tick_pos = [i + (bar_width / 2) for i in bar_l]
    # colors generator
    color = get_color()
    bottom = [0] * len(rates_distribution)

    plt.title('Distribution of assessor rates: Yandex vs Google')
    plt.ylabel('Rates percentage')

    # in case if different companies have different sets of ratenames
    all_rate_names = set()
    for rates in rates_distribution.itervalues():
        for rate_name in rates:
            all_rate_names.add(rate_name)

    rates_lists = {}
    for rates in rates_distribution.itervalues():
        for rate_name in all_rate_names:
            rates_lists.setdefault(rate_name, [])
            rates_lists[rate_name].append(rates.get(rate_name, 0))

    for rate_name, percent in rates_lists.iteritems():
        plt.bar(
            bar_l,
            percent,
            bottom=bottom,
            # it dosn't like labels which start with underscore in some reason
            label=rate_name.strip('_'),
            width=bar_width,
            color=next(color),
        )
        bottom = map(operator.add, bottom, percent)

    plt.xticks(tick_pos, companies)
    plt.legend(loc='best')
    plt.savefig(fname_plot)
    print 'Plot saved as "{fn}"'.format(fn=fname_plot)

if __name__ == '__main__':
    tsv_files = {
        'Yandex': 'yandex_dir.tsv',
        'Google': 'google_dir.tsv',
    }
    counts = {
        company: get_counts_from_file(tsv_file)
        for company, tsv_file in tsv_files.iteritems()
    }
    rates_distribution = {
        company: get_distribution(count)
        for company, count in counts.iteritems()
    }
    samples = {
        company: get_sample(count, 'IRRELEVANT')
        for company, count in counts.iteritems()
    }

    make_plot(rates_distribution)

    # perform Welch’s t-test, which does not assume equal population variane
    _, pvalue = stats.ttest_ind(samples['Yandex'], samples['Google'], equal_var=False)
    print 'pvalue = {}'.format(pvalue)
