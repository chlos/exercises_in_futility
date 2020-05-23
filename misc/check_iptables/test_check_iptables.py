#!/usr/bin/env python
# -*- coding: utf-8 -*-

from check_iptables import (
    iptables_rules_ok,
    iptables_rules_ok_iter
)


def gen_big_out(n):
    out = ''
    for _ in xrange(n):
        out += 'ACCEPT     all  --  192.168.1.1          anywhere\n'
    out += 'ACCEPT     all  --  anywhere             anywhere\n'

    return out


def main():
    # RES MEM: 4795M
    out = gen_big_out(10 ** 8)
    print 'Test data is ready'

    # RES MEM: 14.5G
    # running time: ~47s
    print iptables_rules_ok(out)

    # RES MEM: 4795M
    # running time: ~1m6s
    print iptables_rules_ok_iter(out)


if __name__ == '__main__':
    main()
