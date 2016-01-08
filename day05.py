#!/usr/bin/python

import unittest

def is_nice(word):
	def three_vowels(word):
		vowels = 'aeiou'
		original_length = len(word)
		for vowel in vowels:
			word = word.replace(vowel, '')
		return original_length - len(word) >= 3

	def two_letters_together(word):
		for i in range(len(word) - 1):
			if word[i] == word[i+1]:
				return True
		return False

	def no_verboten_pairs(word):
		return 'ab' not in word and 'cd' not in word and 'pq' not in word and 'xy' not in word

	return three_vowels(word) and two_letters_together(word) and no_verboten_pairs(word)

class TestIsNice(unittest.TestCase):
	def test_smegma(self):
		self.assertTrue(is_nice('ugknbfddgicrmopn'))
		self.assertTrue(is_nice('aaa'))
		self.assertFalse(is_nice('jchzalrnumimnmhp'))
		self.assertFalse(is_nice('haegwjzuvuyypxyu'))
		self.assertFalse(is_nice('dvszwmarrgswjxmb'))

def count_nice_words(filename):
	count = 0
	with open(filename, 'r') as f:
		for line in f:
			count += 1 if is_nice(line) else 0
	return count

if __name__ == '__main__':
	count = count_nice_words('inputs/day05.txt')
	print('{} nice words'.format(count))
	unittest.main()
