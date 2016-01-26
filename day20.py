#!/usr/bin/python

import numpy as np
from sys import argv as argv

def do_problem_part2_efficiently(goal, hint=1000000):
    presents = np.zeros((hint+1,))
    for n in range(2, hint+1):
        for i in range(0,50):
            if n * (i+1) > hint:
                break
            presents[n * (i+1)] += 11 * n
    for i in range(2,hint+1):
        if presents[i] >= goal:
            return i
    return 'no solution found'

def do_problem_efficiently(goal, hint=1000000):
    presents = np.zeros((hint+1,))
    for n in range(2, hint+1):
        for i in range(n, hint+1, n):
            presents[i] += 10 * n
    for i in range(2,hint+1):
        if presents[i] >= goal:
            return i
    return 'no solution found'

if __name__ == '__main__':
    if len(argv) <= 1:
        n = 36000000
    else:
        n = argv[1]
    print(do_problem_part2_efficiently(int(n)))
    print(do_problem_efficiently(int(n)))
