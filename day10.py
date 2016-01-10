#!/usr/bin/python

import unittest

def count_first_char(s):
    first_char = s[0]
    i = 1
    while i < len(s) and s[i] == first_char:
        i += 1
    return i, first_char

def mutate(s):
    new_str = ''
    while s:
        count, c = count_first_char(s)
        s = s[count:]
        new_str += str(count) + c
    return new_str

class TestDay10(unittest.TestCase):
    def test_count_first_char(self):
        assert(count_first_char('11') == (2, '1'))
        assert(count_first_char('1') == (1, '1'))
        assert(count_first_char('111') == (3, '1'))
        assert(count_first_char('11122') == (3, '1'))

    def test_mutate(self):
        assert(mutate('1') == '11')
        assert(mutate('11') == '21')
        assert(mutate('21') == '1211')
        assert(mutate('1211') == '111221')

def do_problem(iterations, s):
    for i in range(iterations):
        s = mutate(s)
    print(len(s))

if __name__ == '__main__':
    do_problem(40, '1113222113')
    unittest.main()
