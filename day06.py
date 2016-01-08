#!/usr/bin/python

from enum import Enum
import numpy as np
import unittest

class Mode(Enum):
	turn_on = 1
	toggle = 2
	turn_off = 3

def classify_mode(instruction):
	if instruction.startswith('turn on'):
		return Mode.turn_on
	elif instruction.startswith('toggle'):
		return Mode.toggle
	elif instruction.startswith('turn off'):
		return Mode.turn_off
	else:
		assert(False)

def classify_range(instruction):
	words = instruction.split(' ')
	boring_words = ['turn', 'on', 'off', 'toggle', 'through']
	new_words = []
	for word in words:
		if word not in boring_words:
			new_words.append(word)
	words = new_words
	assert(len(words) == 2)
	coords = []
	for i in range(len(words)):
		pair = words[i]
		pair.replace('(', '')
		pair.replace(')', '')
		pair = pair.split(',')
		coords.append((int(pair[0]), int(pair[1])))
	return (coords[0], coords[1])

def mutate_board(board, instruction):
	mode = classify_mode(instruction)
	(start, end) = classify_range(instruction)

	for row in range(start[0], end[0]+1):
		for col in range(start[1], end[1]+1):
			if mode == Mode.turn_on:
				board[row][col] = True
			elif mode == Mode.turn_off:
				board[row][col] = False
			elif mode == Mode.toggle:
				board[row][col] = not board[row][col]

def count_lights(filename):
	board = np.zeros((1000,1000), dtype=bool)
	with open(filename, 'r') as f:
		for instruction in f:
			mutate_board(board, instruction)
	print('{} lights on'.format(sum(sum(board))))

class TestSmegma(unittest.TestCase):
	def test_classify_mode(self):
		assert(Mode.turn_off == classify_mode('turn off 499,499 through 500,500'))
		assert(Mode.turn_on == classify_mode('turn on 499,499 through 500,500'))
		assert(Mode.toggle == classify_mode('toggle 499,499 through 500,500'))

	def test_classify_range(self):
		assert(((499,499),(500,500)) == classify_range('turn off 499,499 through 500,500'))

	def test_mutate(self):
		board = np.zeros((1000,1000), dtype=bool)

		mutate_board(board, 'turn on 0,0 through 999,999')
		assert(sum(sum(board)) == 1000000)
		mutate_board(board, 'toggle 0,0 through 999,0')
		assert(sum(sum(board)) == 999000)
		mutate_board(board, 'turn off 999,999 through 999,999')
		assert(sum(sum(board)) == 998999)
		mutate_board(board, 'turn off 0,0 through 999,999')
		assert(sum(sum(board)) == 0)

if __name__ == '__main__':
	count_lights('inputs/day06.txt')
	unittest.main()
