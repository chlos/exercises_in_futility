#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import urlparse

if __name__ == '__main__':

    filename_in = 'urls.txt'
    filename_out = 'urls_hash.txt'
    with open(filename_in, 'r') as file_in, open(filename_out, 'w') as file_out:
        for url in file_in:
            hostname = urlparse.urlparse(url).hostname
            if hostname:
                hashsum = hashlib.md5(url).hexdigest()
                file_out.write('{hostname}\t{hashsum}\n'.format(
                    hostname=hostname, hashsum=hashsum
                ))
            else:
                raise ValueError('Failed to parse hostname. Line:\n{}'.format(url))
