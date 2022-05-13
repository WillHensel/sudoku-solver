"""
This file defines an agent capable of solving a game of Sudoku defined in sudoku.py.
"""
import queue

class AC3Agent:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        # Initialize a queue of binary constraints satisfying alldiff for each unit (row, column, 3x3 box)
        self.binary_constraint_queue = queue.Queue()
        self.initialize_constraint_queue()

    def create_constraint(self, point1, point2):
        constraint = (point1, point2)
        self.binary_constraint_queue.put(constraint)

    def initialize_constraint_queue(self):
        for i in range(9):
            for j in range(9):
                point = (i, j)
                self.push_constraining_neighbors(point)
    
    def ac_3(self):
        while not self.binary_constraint_queue.empty():
            constraint = self.binary_constraint_queue.get()
            if self.revise(constraint):
                node = self.sudoku.get_variable_at_point(constraint[0])
                if len(node[1]) == 0:
                    return False
                self.push_constraining_neighbors(constraint[0], constraint[1])
        return True
    
    def revise(self, constraint):
        point_i = constraint[0]
        point_j = constraint[1]
        node_i = self.sudoku.get_variable_at_point(point_i)
        node_j = self.sudoku.get_variable_at_point(point_j)
        domain_i = node_i[1]
        domain_j = node_j[1]
        revised = False
        for x in domain_i:
            found_satisfier = False
            for y in domain_j:
                if x != y:
                    found_satisfier = True
                    break
            if not found_satisfier:
                domain_i.remove(x)
                revised = True
        return revised

    def push_constraining_neighbors(self, source_point, except_point=None):
        row_unit = self.sudoku.get_row_unit_points(source_point)
        col_unit = self.sudoku.get_col_unit_points(source_point)
        box_unit = self.sudoku.get_box_unit_points(source_point)

        for next_point in row_unit + col_unit + box_unit:
            if next_point != source_point:
                if except_point is not None:
                    if next_point != except_point:
                        self.create_constraint(source_point, next_point)
                    else:
                        break
                self.create_constraint(next_point, source_point)



