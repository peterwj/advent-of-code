#!/usr/bin/python

import copy
import hashlib

key = 'bgvyzdsv'
i = 0
while True:
	hash = hashlib.md5()
	hash.update(key.encode('utf-8'))
	hash.update(str(i).encode('utf-8'))
	if hash.hexdigest()[0:5] == '00000':
		break
	i = i+1

print(i)
