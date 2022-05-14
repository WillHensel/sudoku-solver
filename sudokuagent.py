"""
This file defines an agent capable of solving a game of Sudoku defined in sudoku.py.
"""
import queue

class SudokuAgent:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        # Initialize a queue of binary constraints satisfying alldiff for each unit (row, column, 3x3 box)
        self.binary_constraint_queue = queue.Queue()
        self.initialize_constraint_queue()
        self.unassigned_vars = []

    def ac_3(self):
        while not self.binary_constraint_queue.empty():
            constraint = self.binary_constraint_queue.get()
            if self.revise(constraint):
                node = self.sudoku.get_variable_at_point(constraint[0])
                if len(node.domain) == 0:
                    return False
                self.push_constraining_neighbors(constraint[0], constraint[1])
        return True

    def backtrack(self, assignment):
        if self.check_assignment_complete(assignment):
            return True
        prev = None
        if len(assignment) > 0:
            prev = assignment[len(assignment) - 1]
        var = self.select_unassigned_variable(assignment, prev) # Gets most constrained variable
        for value in self.order_domain_values(var):
            assignment.append(var)
            var.value = value
            self.sudoku.print_grid()
            if self.inference(var):
                self.reduce_dependent_domains(var)
                result = self.backtrack(assignment)
                if result:
                    return result
                self.backtrack_dependent_domains(var)
            assignment.remove(var)
            var.value = None
        return False

    def backtrack_dependent_domains(self, var):
        dependencies = self.get_dependent_positions(var)
        for point in dependencies:
            dependent = self.sudoku.get_variable_at_point(point)
            dependent.domain.append(var.value)

    def backtracking_search(self):
        return self.backtrack([])

    def check_assignment_complete(self, assignment):
        if len(assignment) != len(self.unassigned_vars):
            return False
        
        for x in self.unassigned_vars:
            if x not in assignment:
                return False
        
        return True


    def create_constraint(self, point1, point2):
        constraint = (point1, point2)
        self.binary_constraint_queue.put(constraint)

    def get_dependent_positions(self, var):
        pos = var.position
        row_unit = self.sudoku.get_row_unit_points(pos)
        col_unit = self.sudoku.get_col_unit_points(pos)
        box_unit = self.sudoku.get_box_unit_points(pos)
        dependencies = row_unit + col_unit + box_unit
        return dependencies

    def inference(self, var):
        # Check if value in var is arc-consistent
        dependencies = self.get_dependent_positions(var)
        for point in dependencies:
            dependent = self.sudoku.get_variable_at_point(point)
            if dependent != var:
                if var.value == dependent.value:
                    return False
        return True

    def initialize_constraint_queue(self):
        for i in range(9):
            for j in range(9):
                point = (i, j)
                self.push_constraining_neighbors(point)
    
    def order_domain_values(self, var):
        dependencies = self.get_dependent_positions(var)

        domain = list(var.domain)
        counts = []
        for i, value in enumerate(domain):
            counts.append(0)
            for dependent in dependencies:
                dependent_var = self.sudoku.get_variable_at_point(dependent)
                if value in dependent_var.domain:
                    counts[i] += 1
        if len(domain) != len(counts):
            return domain
        for i in range(len(domain)):
            min_index = i;
            for j in range(i + 1, len(domain)):
                if counts[j] < counts[min_index]:
                    min_index = j
            counts[min_index], counts[i] = counts[i], counts[min_index],
            domain[min_index], domain[i] = domain[i], domain[min_index]
        return domain
        



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
   
    def reduce_dependent_domains(self, var):
        dependencies = self.get_dependent_positions(var)
        for point in dependencies:
            dependent = self.sudoku.get_variable_at_point(point)
            try:
                dependent.domain.remove(var.value)
            except ValueError:
                pass

    def revise(self, constraint):
        point_i = constraint[0]
        point_j = constraint[1]
        node_i = self.sudoku.get_variable_at_point(point_i)
        node_j = self.sudoku.get_variable_at_point(point_j)
        domain_i = node_i.domain
        domain_j = node_j.domain
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

    def select_unassigned_variable(self, assignment, prev):
        selection_set = None
        if prev is not None:
            selection_set = []
            dependents = self.get_dependent_positions(prev)
            if len(dependents) < 2:
                selection_set = None
            else:
                for dependent in dependents:
                    selection_set.append(self.sudoku.get_variable_at_point(dependent))
        if selection_set is None:
            selection_set = self.unassigned_vars
        else:
            for var in selection_set:
                if var not in self.unassigned_vars:
                    selection_set.remove(var)
        most_constrained = None
        for var in self.unassigned_vars:
            if most_constrained is None:
                if var not in assignment:
                    most_constrained = var            
            elif var not in assignment and len(var.domain) < len(most_constrained.domain):
                most_constrained = var
        return most_constrained

    def solve(self):
        reduced = self.ac_3()
        if not reduced:
            return False
        print('Puzzle passed AC_3')

        self.unassigned_vars = []
        continue_to_next_step = False
        for i in range(9):
            for j in range(9):
                var = self.sudoku.get_variable_at_point((i, j))
                if len(var.domain) != 1:
                    self.unassigned_vars.append(var)
                    continue_to_next_step = True
                else:
                    self.sudoku.grid[i][j].value = var.domain[0]
        
        if not continue_to_next_step:
            return True
        
        result = self.backtracking_search()
        return result



