#!/usr/bin/python

from sys import argv as argv
import unittest

class TestDay14(unittest.TestCase):
    def test_basic_case(self):
        lines = [
            'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
            'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
        ]
        reindeer = []
        for line in lines:
            reindeer.append(Reindeer(line))
        assert(calculate_winner(reindeer, 1000) == ('Comet', 1120))

class Reindeer():
    def __init__(self, sentence):
        sentence = sentence.split(' ')
        self.name = sentence[0]
        self.distance = int(sentence[3])
        self.moving_time = int(sentence[6])
        self.resting_time = int(sentence[13])

def calculate_distance(reindeer, total_time):
    period_length = reindeer.moving_time + reindeer.resting_time
    complete_moving_periods = total_time // period_length
    leftover_time = total_time - complete_moving_periods * period_length
    leftover_moving_time = min(reindeer.moving_time, leftover_time)
    return (complete_moving_periods * reindeer.moving_time + leftover_moving_time) * reindeer.distance

def calculate_winner(reindeer, total_time):
    winner = (reindeer[0].name, calculate_distance(reindeer[0], total_time))
    for rd in reindeer:
        rd_score = calculate_distance(rd, total_time)
        if rd_score > winner[1]:
            winner = (rd.name, rd_score)
    return winner

if __name__ == '__main__':
    if len(argv) == 3:
        filename = argv[1]
        total_time = int(argv[2])
        with open(filename) as f:
            reindeer = []
            for line in f:
                reindeer.append(Reindeer(line))
            print(calculate_winner(reindeer, total_time))
    else:
        unittest.main()
