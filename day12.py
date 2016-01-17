#!/usr/bin/python

import json
from sys import argv as argv
import types
import unittest

class TestDay12(unittest.TestCase):
    def test_sum_numbers_in_dict(self):
        cases = [
                ('[1,2,3]', 6),
                ('{"a":2,"b":4}', 6),
                ('{"a":{"b":4},"c":-1}', 3),
                ('[]', 0),
        ]
        for case,expected in cases:
            assert(sum_numbers_in_dict(json.loads(case)) == expected)

    def test_sum_numbers_in_dict_ignore_red(self):
        cases = [
                ('[1,2,3]', 6),
                ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
                ('[1,{"c":"red","b":2},3]', 4),
                ('[1,"red",5]', 6),
                ('[]', 0),
        ]
        for case,expected in cases:
            assert(sum_numbers_in_dict(json.loads(case), 'red') == expected)

def sum_numbers_in_dict(d, ignore_str=None):
    if isinstance(d, str):
        return 0
    elif isinstance(d, int):
        return d
    elif isinstance(d, list):
        sum = 0
        for item in d:
            sum += sum_numbers_in_dict(item, ignore_str)
        return sum
    elif isinstance(d, dict):
        sum = 0
        for k,v in d.items():
            if ignore_str and v == ignore_str:
                return 0
            sum += sum_numbers_in_dict(k, ignore_str) + sum_numbers_in_dict(v, ignore_str)
        return sum
    print('invalid type {}'.format(type(d)))
    assert(False)

if __name__ == '__main__':
    if len(argv) > 1:
        with open(argv[1], 'r') as f:
            d = json.load(f)
            print(sum_numbers_in_dict(d))
            print(sum_numbers_in_dict(d, ignore_str='red'))
    else:
        unittest.main()
