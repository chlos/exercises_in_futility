#!/usr/bin/env python
# -*- coding: utf-8 -*-


def maximum69Number(num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        for i in xrange(0, len(str_num)):
            digit = int(str_num[i])
            print i, digit
            if digit == 6:
                print 'it is 6'
                mult = 10 ** (len(str_num) - 1 - i)
                num = num - mult * 6 + mult * 9
                break

        print num
        return num


if __name__ == "__main__":
    assert maximum69Number(6999) == 9999
    assert maximum69Number(9699) == 9999
    assert maximum69Number(9969) == 9999
    assert maximum69Number(9996) == 9999
    assert maximum69Number(9999) == 9999
    print 'OK'
