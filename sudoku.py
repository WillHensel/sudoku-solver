"""
This file defines the game of sudoku.
"""
import math
import os

class Sudoku:

    def __init__(self, initialConstraints):
        
        # Initialize a game grid
        initialDomain = [1,2,3,4,5,6,7,8,9]
        self.grid = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(Variable((i, j), None, list(initialDomain)))
            self.grid.append(row)

        # Setup this puzzle's unique unary constraints
        for value in initialConstraints:
            point = value[0]
            self.grid[point[0]][point[1]] = Variable(point, None, [value[1]])

    def contains_blanks(self):
        for i in range(9):
            for j in range(9):
                var = self.get_variable_at_point((i, j))
                if var.value is None:
                    return True
        return False

    def get_variable_at_point(self, point):
        return self.grid[point[0]][point[1]]

    def get_all_unit_points(self, point):
        return self.get_row_unit_points(point) + self.get_col_unit_points(point) + self.get_box_unit_points(point)

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

    def print_domain_size_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(9):
            if i != 0 and i % 3 == 0:
                print(str('-') * 7 * 3)
            for j in range(9):
                if j != 0 and j % 3 == 0:
                    print('|', end=' ')
                size = len(self.grid[i][j].domain)
                print(size, end=' ')
            print()

    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(9):
            if i != 0 and i % 3 == 0:
                print(str('-') * 7 * 3)
            for j in range(9):
                if j != 0 and j % 3 == 0:
                    print('|', end=' ')
                var = self.grid[i][j]
                if var.value is None:
                    print('*', end=' ')
                else:
                    print(var.value, end=' ')
            print()

    def verify_validity(self):
        for row in self.grid:
            for var in row:
                dependent_points = self.get_all_unit_points(var.position)
                for point in dependent_points:
                    dependent_var = self.get_variable_at_point(point)
                    if dependent_var is not var:
                        if var.value == dependent_var.value:
                            return False
        return True


class Variable:

    def __init__(self, position, value, domain):
        self.position = position
        self.value = value
        self.domain = domain
