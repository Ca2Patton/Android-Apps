#!/usr/bin/env python
"""
Playing with empty classes
"""

class Employee:
	pass

john = Employee()
john.name = "John Doe"
john.dept = 'computer lab'
john.salary = 1000

print john.name

#Question: Why would you need an empty class?
