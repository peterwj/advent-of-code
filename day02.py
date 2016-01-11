#!/usr/bin/python

from sys import argv as argv
import unittest

def compute_paper(dims):
    assert(len(dims) == 3)
    l,w,h = dims
    areas = (l*w, w*h, l*h)
    return 2*sum(areas) + min(areas)

def compute_ribbon(dims):
    assert(len(dims) == 3)
    l,w,h = dims
    perims = (l+w, w+h, l+h)
    return 2*min(perims) + l*w*h

class TestDay2(unittest.TestCase):
    def test_paper(self):
        assert(compute_paper((2,3,4,)) == 58)
        assert(compute_paper((1,1,10)) == 43)
    def test_ribbon(self):
        assert(compute_ribbon((2,3,4)) == 34)
        assert(compute_ribbon((1,1,10)) == 14)

def run_program(filename):
    ribbon, paper = 0, 0
    with open(filename) as f:
        for line in f:
            line = line.split('x')
            assert(len(line) == 3)
            dims = (int(line[0]), int(line[1]), int(line[2]))
            ribbon += compute_ribbon(dims)
            paper += compute_paper(dims)
    print('{} paper'.format(paper))
    print('{} ribbon'.format(ribbon))

if __name__ == '__main__':
    run_program('inputs/day02.txt')
    unittest.main()
