#!/usr/bin/env python
import unittest

def foo():
	raise OSError

class TestingIsFun(unittest.TestCase):
	def setUp(self):
		print 'stp'
	
	def runTest(self):
		print 'stp'

	def test_upper(self):
		self.assertEqual(2+2, 4)

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)
	
	def test_exception(self):
		self.assertRaises(OSError,foo)
	
def suite():
	test_suite = unittest.TestSuite()
	test_suite.addTest(unittest.makeSuite(TestingIsFun))
	return test_suite
mySuite=suite()


if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(mySuite)
