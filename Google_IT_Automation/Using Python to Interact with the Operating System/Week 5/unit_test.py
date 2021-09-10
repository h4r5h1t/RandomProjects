'''
Imagine one of your IT coworkers just retired and left a folder of scripts for you to use. One of the scripts, called emails.py, matches users to an email address and lets us easily look them up! For the most part, the script works great — you enter in an employee's name and their email is printed to the screen. But, for some employees, the output doesn't look quite right. Your job is to add a test to reproduce the bug, make the necessary corrections, and verify that all the tests pass to make sure the script works! Best of luck!
'''

#!/usr/bin/env python3
import unittest

form emails import find_email

class EmailTest(unittest.TestCase):
	def test_basic(self):
		testcase = [None, "Bree", "Cambell"]
		expected = "breee@abc.edu"
		self.assertEqual(find_email(testcase), expected)
	def test_one_name(self):
		testcase = [None, "John"]
		expected = "Missing parameters"
		self.assertEqual(find_email(testcase), expected)

	def test_notin_name(slef):
		testcase = [None, "Harshit", "Singh"]
		expected = "No email address found"
		self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
	unittest.main()

