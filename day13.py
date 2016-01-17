#!/usr/bin/python

from itertools import permutations
from sys import argv as argv
import unittest

class TestDay13(unittest.TestCase):
    def test_basic_case(self):
        matrix = parse_input_file('inputs/day13-test.txt')
        assert(find_optimal_seating(matrix) == 330)

def parse_input_file(filename):
    adjacency_matrix = {}
    with open(filename) as f:
        for line in f:
            line = line.split(' ')
            this_person = line[0]
            other_person = line[10].replace('.', '').replace('\n', '')
            is_increase = line[2] == 'gain'
            magnitude = int(line[3]) if is_increase else -int(line[3])
            if this_person not in adjacency_matrix:
                adjacency_matrix[this_person] = {other_person: magnitude}
            else:
                adjacency_matrix[this_person][other_person] = magnitude
    return adjacency_matrix

def find_optimal_seating(matrix):
    names = matrix.keys()
    candidates = permutations(names)
    best_score = 0
    for candidate in candidates:
        score = 0
        for idx, name in list(enumerate(candidate)):
            before_neighbor = candidate[idx-1]
            after_neighbor = candidate[idx+1-len(candidate)] # wrap around
            score += matrix[name][before_neighbor] + matrix[name][after_neighbor]
        if score > best_score:
            best_score = score
    return best_score


if __name__ == '__main__':
    if len(argv) == 2:
        matrix = parse_input_file(argv[1])
        print(find_optimal_seating(matrix))
    else:
        unittest.main()
