#!/usr/bin/env python3
import os
import snakes_and_ladders
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)

class TestSnakes(unittest.TestCase):
	def test_sandl_0(self):
		finalVal = 100
		ladders = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
		snakes = {32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:78}
		result = snakes_and_ladders.snakesAndLadders(finalVal, snakes, ladders)
		self.assertEqual(result, 6)

	def test_sandl_1(self):
		finalVal = 42
		ladders = {2:15, 7:28, 14:27, 19:32, 25:38}
		snakes = {10:6, 13:3, 30:9, 35:21, 41:24}
		result = snakes_and_ladders.snakesAndLadders(finalVal, snakes, ladders)
		self.assertEqual(result, 4)

	def test_sandl_2(self):
		finalVal = 10
		ladders = {1:10}
		snakes = {}
		result = snakes_and_ladders.snakesAndLadders(finalVal, snakes, ladders)
		self.assertEqual(result, 1)

	def test_sandl_3(self):
		finalVal = 34
		ladders = {}
		snakes = {}
		result = snakes_and_ladders.snakesAndLadders(finalVal, snakes, ladders)
		self.assertEqual(result, 6)

	def test_sandl_4(self):
		finalVal = 100
		ladders = {2:24, 4:25, 7:16, 8:29, 14:33, 23:42, 30:49, 35:48,
				   37:76, 63:99, 66:87, 69:94, 72:91}
		snakes = {11:6, 21:3, 26:5, 36:17, 53:50, 55:45, 58:38, 62:41,
				  64:56, 77:12, 93:70, 96:68, 98:30}
		result = snakes_and_ladders.snakesAndLadders(finalVal, snakes, ladders)
		self.assertEqual(result, 6)

	def test_sandl_5(self):
		finalVal = 100
		ladders = {80:99, 1:38, 51:67, 4:14, 21:42, 72:91, 9:31, 28:84}
		snakes = {64:60, 17:7, 98:79, 54:34, 87:36, 93:73, 62:19, 95:75}
		result = snakes_and_ladders.snakesAndLadders(finalVal, snakes, ladders)
		self.assertEqual(result, 7)

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
