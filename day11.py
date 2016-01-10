#!/usr/bin/python

import unittest

class TestDay11(unittest.TestCase):
    def test_check_validity(self):
        assert(includes_run('hijklmmn'))
        self.assertFalse(no_verboten_letters('hijklmmn'))
        assert(includes_two_pairs('abbceffg'))
        self.assertFalse(includes_run('abbceffg'))
    def test_next_password(self):
        assert(next_password('xz') == 'ya')
        assert(next_password('xx') == 'xy')
    def test_find_new_password(self):
        assert(find_new_password('abcdefgh') == 'abcdffaa')
        assert(find_new_password('ghijklmn') == 'ghjaabcc')

def check_validity(password):
    return (
            includes_run(password) and
            no_verboten_letters(password) and
            includes_two_pairs(password)
    )

def no_verboten_letters(password):
    return (
            'i' not in password and
            'o' not in password and
            'l' not in password
    )

def includes_run(password):
    for i in range(len(password) - 2):
        if (
                ord(password[i]) == ord(password[i+1]) - 1 and
                ord(password[i]) == ord(password[i+2]) - 2
        ):
            return True
    return False

def includes_two_pairs(password):
    first = find_pair(password)
    if not first:
        return False
    second = find_pair(password, forbidden=first)
    if not second:
        return False
    return True

def find_pair(password, forbidden=None):
    for i in range(len(password) - 1):
        if password[i] == password[i+1] and password[i] != forbidden:
            return password[i]
    return None

def find_new_password(password):
    password = next_password(password)
    while not check_validity(password):
        password = next_password(password)
    return password

def next_password(password):
    password = list(password)
    carry = False
    i = len(password) - 1
    c = ord(password[i]) + 1
    while i >= 0:
        if c <= ord('z'):
            password[i] = chr(c)
            break
        else:
            password[i] = 'a'
            i -= 1
            c = ord(password[i]) + 1
    return "".join(password)

if __name__ == '__main__':
    print(find_new_password('hepxcrrq'))
    unittest.main()
