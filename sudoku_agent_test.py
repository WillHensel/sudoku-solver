import unittest

from sudoku import *
from sudokuagent import *

testGrid = [
        ((0, 1), 2), ((0, 2), 9), ((0, 5), 5), ((0, 6), 1), ((0, 7), 7),
        ((1, 1), 5), ((1, 2), 8), ((1, 4), 2), ((1, 5), 6), ((1, 6), 9), ((1, 8), 3),
        ((2, 0), 3), ((2, 6), 6), ((2, 8), 2),
        ((3, 3), 4), ((3, 4), 7), ((3, 5), 9), ((3, 8), 1),
        ((4, 0), 4), ((4, 3), 1), ((4, 4), 6),
        ((5, 0), 9), ((5, 3), 5), ((5, 5), 8), ((5, 6), 4),
        ((6, 0), 8), ((6, 3), 9), ((6, 7), 2), ((6, 8), 4),
        ((7, 1), 4), ((7, 2), 3), ((7, 5), 7), ((7, 7), 1),
        ((8, 4), 5), ((8, 5), 4), ((8, 6), 3), ((8, 7), 8), ((8, 8), 6)
    ]

class TestSudokuAgent(unittest.TestCase):

    def test_initialize_constraints_queue(self):
        sudoku = Sudoku(testGrid)
        sudoku_agent = AC3Agent(sudoku)
        constraints = sudoku_agent.binary_constraint_queue
        # Pick some row constraints to test
        self.assertIn(((0,0), (0,1)), constraints)
        self.assertIn(((0,1), (0,0)), constraints)
        self.assertIn(((8,7), (8,8)), constraints)
        self.assertIn(((8,8), (8,7)), constraints)
        # Pick some column constraints to test
        self.assertIn(((0,0), (1,0)), constraints)
        self.assertIn(((1,0), (0,0)), constraints)
        self.assertIn(((7,8), (8,8)), constraints)
        self.assertIn(((8,8), (7,8)), constraints)
        # Pick some box constraints to test that wouldn't be a row or column constraint
        self.assertIn(((0,0), (1,2)), constraints)
        self.assertIn(((1,2), (0,0)), constraints)
        self.assertIn(((8,8), (7,7)), constraints)
        self.assertIn(((7,7), (8,8)), constraints)
        # Spot check for invalid constraints
        self.assertNotIn(((0,0), (1,3)), constraints)
        self.assertNotIn(((1,3), (0,0)), constraints)

if __name__ == '__main__':
    unittest.main()