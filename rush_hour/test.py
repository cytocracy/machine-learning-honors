#!/usr/bin/env python3
import os
import rush
import helper
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)

class TestInitialize(unittest.TestCase):
	def test_make_cars(self):
		board = [[-1, -1, -1, 1, -1, -1], 
				 [-1, -1, -1, 1, -1, -1], 
				 [0, 0, -1, 1, -1, -1], 
				 [-1, -1, -1, -1, -1, -1], 
				 [-1, 2, -1, -1, -1, -1], 
				 [-1, 2, 3, 3, 4, 4]]
		correct = {0: [(2, 0), (2, 1)], 
				   1: [(0, 3), (1, 3), (2, 3)], 
				   2: [(4, 1), (5, 1)], 3: [(5, 2), (5, 3)], 4: [(5, 4), (5, 5)]}
		result = rush.makeCars(board)
		self.assertTrue(-1 not in result, "-1 is not a car.")
		self.assertEqual(len(result), len(correct), "Wrong number of cars")
		self.assertEqual(correct, result, "incorrect dictionary")

	def test_make_board(self):
		cars = {0: [(2, 0), (2, 1)], 
			   1: [(0, 3), (1, 3), (2, 3)], 
			   2: [(4, 1), (5, 1)], 3: [(5, 2), (5, 3)], 4: [(5, 4), (5, 5)]}
		correct = [[-1, -1, -1, 1, -1, -1], 
				 [-1, -1, -1, 1, -1, -1], 
				 [0, 0, -1, 1, -1, -1], 
				 [-1, -1, -1, -1, -1, -1], 
				 [-1, 2, -1, -1, -1, -1], 
				 [-1, 2, 3, 3, 4, 4]]
		result = rush.makeBoard(cars)
		self.assertEqual(len(result), 6, "wrong number of rows")
		self.assertEqual(len(result[0]), 6, "wrong number of columns")
		self.assertEqual(correct, result, "incorrect board")

class TestSuccessors(unittest.TestCase):
	def test_successors_0(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/easy.txt"))
		result = rush.getSuccessors(board)
		self.assertEqual(len(result), 3, "incorrect number of successors")

	def test_successors_1(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/1.txt"))
		result = rush.getSuccessors(board)
		self.assertEqual(len(result), 7, "incorrect number of successors")

	def test_successors_2(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/hard.txt"))
		result = rush.getSuccessors(board)
		self.assertEqual(len(result), 3, "incorrect number of successors")

	def test_successors_3(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/27.txt"))
		result = rush.getSuccessors(board)
		self.assertEqual(len(result), 1, "incorrect number of successors")

	def test_successors_4(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/13.txt"))
		result = rush.getSuccessors(board)
		self.assertEqual(len(result), 6, "incorrect number of successors")

	def test_successors_5(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/22.txt"))
		result = rush.getSuccessors(board)
		self.assertEqual(len(result), 5, "incorrect number of successors")

class TestBFS(unittest.TestCase):
	def test_bfs_0(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/easy.txt"))
		result, numExpanded = rush.BFS(board)
		self.assertTrue(board==result[0], "First state in the path is wrong")
		self.assertTrue(result[-1][2][5]==0, "Last state in path is not a goal state")
		self.assertEqual(len(result), 10)

	def test_bfs_1(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/1.txt"))
		result, numExpanded = rush.BFS(board)
		self.assertTrue(board==result[0], "First state in the path is wrong")
		self.assertTrue(result[-1][2][5]==0, "Last state in path is not a goal state")
		self.assertEqual(len(result), 17)

	def test_bfs_2(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/20.txt"))
		result, numExpanded = rush.BFS(board)
		self.assertTrue(board==result[0], "First state in the path is wrong")
		self.assertTrue(result[-1][2][5]==0, "Last state in path is not a goal state")
		self.assertEqual(len(result), 19)

	def test_bfs_3(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/hard.txt"))
		result, numExpanded = rush.BFS(board)
		self.assertTrue(board==result[0], "First state in the path is wrong")
		self.assertTrue(result[-1][2][5]==0, "Last state in path is not a goal state")
		self.assertEqual(len(result), 25)

	def test_bfs_4(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/Solved.txt"))
		result, numExpanded = rush.BFS(board)
		self.assertTrue(board==result[0], "First state in the path is wrong")
		self.assertTrue(result[-1][2][5]==0, "Last state in path is not a goal state")
		self.assertEqual(len(result), 1)

	def test_bfs_5(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/31.txt"))
		result, numExpanded = rush.BFS(board)
		self.assertTrue(board==result[0], "First state in the path is wrong")
		self.assertTrue(result[-1][2][5]==0, "Last state in path is not a goal state")
		self.assertEqual(len(result), 70)

	def test_bfs_6(self):
		board = rush.makeBoard(helper.loadPuzzle("jams/39.txt"))
		result, numExpanded = rush.BFS(board)
		self.assertTrue(board==result[0], "First state in the path is wrong")
		self.assertTrue(result[-1][2][5]==0, "Last state in path is not a goal state")
		self.assertEqual(len(result), 83)

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)