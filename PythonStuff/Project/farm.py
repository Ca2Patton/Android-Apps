#!/usr/bin/env python

import unittest

#What is a farm object?
"""
Farm has outgoing, and ingoing
Has counters for outgoing, ingoing, stay, and invalid.
Has things that cannot leave the farm.
"""

class Farm():
	"""
	This defines a farm object.
	"""

	def __init__(self):
		self.totals = {
                                'outgoing': 0,
				
				}
	
	def recvData(self, key, value):
		"""
		Receive data on incoming farms
		"""
		assert key in self.totals, "Key not in Dictionary."
		assert isinstance(value, int), "Value must be an int."
		self.setTotals(key, value)

	def setTotals(self, key=None, value=None):
		assert key in self.totals, "Key does not exist in dictionary"
		assert isinstance(value, int), "Value must be an int"
		self.totals[key] = value
	
	def getTotals(self, key=None):
		assert key in self.totals, "Key does not exist in dictionary."
		return self.totals[key]

class TestFarmMethods(unittest.TestCase):

	def setUp(self):
		self.farm = Farm()

	def test_recv(self):
		self.farm.recvData('outgoing', 1820)
		self.assertEqual(self.farm.getTotals('outgoing'), 1820)


if __name__ == '__main__':
	f = Farm()
	f.recvData('outgoing', 182)
	unittest.main()
