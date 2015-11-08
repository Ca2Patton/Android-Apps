#!/usr/bin/env python

n = raw_input("Number? ")
n2 = int(n)
def funWithGenerators(n):
	i = 0
	while i < n:
		yield i
		i+= 1
#How do I print my iterator?

foo = funWithGenerators(n2)
print foo.next()
print foo.next()

#Nevermind, remembers I had to call my func. >.>
