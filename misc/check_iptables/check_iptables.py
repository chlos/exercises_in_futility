#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import subprocess


def get_iptables_out(chain):
    '''
    We can improve it with buffering to avoid O(N) extra space complexity:
    https://stackoverflow.com/a/5605597/2641804
    '''
    p = subprocess.Popen(
        ['iptables', '-L', chain],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = p.communicate()
    return out


def iptables_rules_ok(iptables_out):
    '''
    2x additional space needed, but non-generator splitlines() is faster
    '''
    for line in iptables_out.splitlines():
        rule = line.split()
        try:
            target, source = rule[0], rule[3]
        except IndexError:
            pass

        if target == 'ACCEPT' and source == 'anywhere':
            return False

    return True


def splitlines_iter(s):
    return (x.group(0) for x in re.finditer(r"(.*\n|.+$)", s))


def iptables_rules_ok_iter(iptables_out):
    '''
    No additional space needed, but more cpu overhead on each split line
    '''
    for line in splitlines_iter(iptables_out):
        rule = line.split()
        try:
            target, source = rule[0], rule[3]
        except IndexError:
            pass

        if target == 'ACCEPT' and source == 'anywhere':
            return False

    return True


def main():
    iptables_out = get_iptables_out('INPUT')
    if iptables_rules_ok_iter(iptables_out):
        print 'OK'
    else:
        print 'Not OK'
        exit(1)


if __name__ == '__main__':
    main()
