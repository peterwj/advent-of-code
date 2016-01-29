#!/usr/bin/python
import math
import numpy as np
from sys import argv as argv
from unittest import main, TestCase

class TestDay1(TestCase):
    def test_calculate_floor(self):
        assert(calculate_floor('(())') == 0)
        assert(calculate_floor('))(((((') == 3)
    def test_calculate_floor_basement(self):
        assert(calculate_floor(')', basement_mode=True) == 1)
        assert(calculate_floor('()())', basement_mode=True) == 5)

def calculate_floor(paren_string, basement_mode=False):
    result = 0
    for (i,c) in enumerate(paren_string):
        if c == '(':
            result += 1
        elif c == ')':
            result -= 1
        else:
            assert(False)
        if basement_mode and result < 0:
            return i+1
    return result

if __name__ == '__main__':
    if len(argv) == 1:
        main()
    elif len(argv) == 2:
        input_string = argv[1]
        print(calculate_floor(input_string))
        print(calculate_floor(input_string, basement_mode=True))
    else:
        print('Usage: `{} paren_string`'.format(argv[0]))
