# This script checkc whether a string contains a set of characters

import itertools

def containsAny(seq, aset):
	return bool(set(aset).intersection(seq))

a_string = ["z", "c", "b"]
a_set = ['a', 'a', 'd', 'c', 'b']

print(containsAny(a_string, a_set))