#!/usr/bin/env python3
import os
import knight_moves
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)

class TestKnight(unittest.TestCase):
	def test_knight_0(self):
		startingLocation = (2,5)
		endingLocation = (1,3)
		result = knight_moves.minKnightMoves(startingLocation, endingLocation)
		self.assertEqual(result, 1)

	def test_knight_1(self):
		startingLocation = (1,3)
		endingLocation = (5,0)
		result = knight_moves.minKnightMoves(startingLocation, endingLocation)
		self.assertEqual(result, 3)

	def test_knight_2(self):
		startingLocation = (4,7)
		endingLocation = (4,7)
		result = knight_moves.minKnightMoves(startingLocation, endingLocation)
		self.assertEqual(result, 0)

	def test_knight_3(self):
		startingLocation = (0,0)
		endingLocation = (7,7)
		result = knight_moves.minKnightMoves(startingLocation, endingLocation)
		self.assertEqual(result, 6)

	def test_knight_4(self):
		startingLocation = (2,3)
		endingLocation = (2,4)
		result = knight_moves.minKnightMoves(startingLocation, endingLocation)
		self.assertEqual(result, 3)

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)