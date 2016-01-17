#!/usr/bin/python

import unittest

class TestDay17(unittest.TestCase):
    def test_basic_case(self):
        combos = compute_combinations(25, [20,15,10,5,5])
        assert(len(combos) == 4)
    def test_part_ii(self):
        combos = compute_combinations(25, [20,15,10,5,5])
        assert(do_part_ii(25, [20,15,10,5,5]) == 3)

def compute_combinations(n, sizes):
    if n == 0:
        return [[]]
    if n < 0 or sizes == []:
        return []
    inclusive_solutions = [[sizes[0]] + s for s in compute_combinations(n-sizes[0], sizes[1:])]
    exclusive_solutions = compute_combinations(n, sizes[1:])
    return inclusive_solutions + exclusive_solutions

def do_part_ii(n, sizes):
    combos = compute_combinations(n, sizes)
    shortest_length = min([len(c) for c in combos])
    combos = [c for c in combos if len(c) == shortest_length]
    return len(combos)

def do_problem(filename):
    sizes = []
    with open(filename) as f:
        for line in f:
            sizes.append(int(line))
    print(len(compute_combinations(150, sizes)))
    print(do_part_ii(150, sizes))

if __name__ == '__main__':
    do_problem('inputs/day17.txt')
    unittest.main()
