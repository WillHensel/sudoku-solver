"""
This file defines an agent capable of solving a game of Sudoku defined in sudoku.py.
"""

class AC3Agent:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        # Initialize a queue of binary constraints satisfying alldiff for each unit (row, column, 3x3 box)
        self.binary_constraint_queue = []
        self.initialize_constraint_queue(self.binary_constraint_queue)
        print(len(self.binary_constraint_queue))

    def create_constraint(self, point1, point2, queue):
        forward_constraint = (point1, point2)
        backward_constraint = (point2, point1)
        if forward_constraint not in queue:
            queue.append(forward_constraint)
        if backward_constraint not in queue:
            queue.append(backward_constraint)

    def initialize_constraint_queue(self, queue):

        for i in range(9):
            for j in range(9):
                point = (i, j)
                row_unit = self.sudoku.get_row_unit_points(point)
                col_unit = self.sudoku.get_col_unit_points(point)
                box_unit = self.sudoku.get_box_unit_points(point)

                for next_point in row_unit:
                    if next_point != point:
                        self.create_constraint(point, next_point, queue)

                for next_point in col_unit:
                    if next_point != point:
                        self.create_constraint(point, next_point, queue)
                
                for next_point in box_unit:
                    if next_point != point:
                        self.create_constraint(point, next_point, queue)
    
    def ac_3(self):
        while len(self.binary_constraint_queue) > 0:
            constraint = self.binary_constraint_queue.pop(0)
            if self.revise(constraint):
                node = self.sudoku.get_variable_at_point(constraint[0])
                if len(node[1]) == 0:
                    return False
                self.find_constraining_neighbors(constraint[0])
        return True
    
    def revise(self, constraint):
        node_i = self.sudoku.get_variable_at_point(constraint[0])
        node_j = self.sudoku.get_variable_at_point(constraint[1])
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

    def find_constraining_neighbors(self, point):

        row_unit = self.sudoku.get_row_unit_points(point)
        col_unit = self.sudoku.get_col_unit_points(point)
        box_unit = self.sudoku.get_box_unit_points(point)

        for next_point in row_unit:
            if next_point != point:
                self.create_constraint(point, next_point, self.binary_constraint_queue)

        for next_point in col_unit:
            if next_point != point:
                self.create_constraint(point, next_point, self.binary_constraint_queue)
        
        for next_point in box_unit:
            if next_point != point:
                self.create_constraint(point, next_point, self.binary_constraint_queue)


