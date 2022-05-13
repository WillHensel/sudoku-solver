"""
This file defines the game of sudoku.
"""
import math

class Sudoku:

    def __init__(self, initialConstraints):
        
        # Initialize a game grid
        initialDomain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.grid = []
        for _ in range(9):
            row = []
            for _ in range(9):
                row.append((None, list(initialDomain)))
            self.grid.append(row)

        # Setup this puzzle's unique unary constraints
        for value in initialConstraints:
            point = value[0]
            self.grid[point[0]][point[1]] = (None, [value[1]])

    def get_variable_at_point(self, point):
        return self.grid[point[0]][point[1]]

    def get_row_unit_points(self, point):
        unit = []
        for i in range(9):
            unit.append((point[0], i))
        return unit

    def get_col_unit_points(self, point):
        unit = []
        for i in range(9):
            unit.append((i, point[1]))
        return unit

    def get_box_unit_points(self, point):
        unit = []
        boxX = math.floor(point[0] / 3)
        boxY = math.floor(point[1] / 3)
        boxX_offset = boxX * 3
        boxY_offset = boxY * 3

        for i in range(3):
            for j in range(3):
                unit.append((boxX_offset + i, boxY_offset + j))
        return unit

    