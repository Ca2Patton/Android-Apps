#!/usr/bin/env python

n = raw_input("Number? ")

def funWithGenerators(n):
	i = 0
	while i < n:
		yield i
		i+= 1
#How do I print my iterator?
