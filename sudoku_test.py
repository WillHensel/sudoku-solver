import unittest

from sudoku import *

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

class TestSudoku(unittest.TestCase):

    def test_get_row_unit_points(self):
        sudoku = Sudoku(testGrid)
        row_points = sudoku.get_row_unit_points((0, 0))
        expected = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
        self.assertCountEqual(row_points, expected)

    def test_get_col_unit_points(self):
        sudoku = Sudoku(testGrid)
        col_points = sudoku.get_col_unit_points((0, 0))
        expected = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
        self.assertCountEqual(col_points, expected)

    def test_get_box_unit_points(self):
        sudoku = Sudoku(testGrid)
        box_points = sudoku.get_box_unit_points((0, 0))
        expected = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.assertCountEqual(box_points, expected)
        box_points = sudoku.get_box_unit_points((7,7))
        expected = [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
        self.assertCountEqual(box_points, expected)

if __name__ == '__main__':
    unittest.main()