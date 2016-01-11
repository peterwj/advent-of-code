#!/usr/bin/python

import copy
import hashlib
from sys import argv as argv

def do_calcs(key, zerocount):
    result = '0' * zerocount
    i = 0
    while True:
        hash = hashlib.md5()
        hash.update(key.encode('utf-8'))
        hash.update(str(i).encode('utf-8'))
        if hash.hexdigest()[0:zerocount] == result:
            break
        i = i+1
    return i

if __name__ == '__main__':
    if len(argv) <= 1:
        zerocount = 5
    else:
        zerocount = int(argv[1])

    print(do_calcs('bgvyzdsv', zerocount))

