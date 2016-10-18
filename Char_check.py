# Char_check.py script checks whether a string contains a set of characters.
# -*- coding: utf-8 -*-

# Function to iterate

def containsAny(seq, aset):
	for c in seq:		# iterate through each item in seq using iterator object
		if c in aset:	# Use of *in* boolean operator to test membership of a sequence
			print c
			return True
	return False

a_string = ["z", "c", "b"]
a_set = ['a', 'a', 'd', 'c', 'b']

print (containsAny(a_string, a_set))