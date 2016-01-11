#!/usr/bin/python

import unittest

class TestDay8(unittest.TestCase):
    def test_(self):
        lines = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
        assert(do_problem(lines) == 12)

def do_problem(lines):
    code = 0
    data = 0
    for line in lines:
        code += len(line)
        i = 1 #skip leading "
        while i < len(line) - 1: # skip trailing "
            if line[i] != '\\':
                data += 1
            else:
                i += 1
                if line[i] in ('\\', '"'):
                    data += 1
                elif line[i] == 'x':
                    data += 1
                    i += 2
                else:
                    assert(False)
            i += 1

    return code - data

if __name__ == '__main__':
    with open('inputs/day08.txt', 'r') as f:
        lines = f.readlines()
    print(do_problem(lines))
    unittest.main()
