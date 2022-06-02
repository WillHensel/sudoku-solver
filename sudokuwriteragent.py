import random
import time

from sudoku import *
from sudokusolveragent import *

class SudokuWriterAgent:

    def __init__(self):
        random.seed = time.time()
        self.sudoku = Sudoku([])

    def backtrack_assignments(self, deassignments):
        if 81 - len(deassignments.keys()) <= 20:
            return True
        self.sudoku.print_grid()
        variables = self.get_assigned_variables()
        random.shuffle(variables)
        for var in variables:
            deassignments[var] = var.value
            self.update_dependent_domains_before_deassignment(var)
            var.value = None
            if self.check_for_unique_solution(var.position[0], var.position[1]):
                result = self.backtrack_assignments(deassignments)
                if result:
                    return result
            var.value = deassignments[var]
            del deassignments[var]
            self.update_dependent_domains_after_reassignment(var)
            # variables = self.get_assigned_variables()
            random.shuffle(variables)
        return False


    def check_for_unique_solution(self, row, col):
        solution_count = self.solve(row, col, 0)
        if solution_count > 2 or solution_count == 0:
            return False
        return True

    def create_solution(self):
        unassigned_vars = []
        for i in range(9):
            for j in range(9):
                var = self.sudoku.get_variable_at_point((i, j))
                if var.value is None:
                    unassigned_vars.append(var)

        index = random.randrange(0, len(unassigned_vars))
        first_assignment = unassigned_vars[index]
        first_assignment.value = random.randrange(1, 9)
        solver_agent = SudokuSolverAgent(self.sudoku)
        solver_agent.unassigned_vars = unassigned_vars
        solver_agent.reduce_dependent_domains(first_assignment)
        solver_agent.unassigned_vars.remove(first_assignment)
        solver_agent.backtrack([first_assignment], self.order_domain_values)

    def get_assigned_variables(self):
        unassigned = []
        for row in self.sudoku.grid:
            for var in row:
                if var.value is not None:
                    unassigned.append(var)
        return unassigned

    def legal(self, row, col, val):
        var = self.sudoku.get_variable_at_point((row, col))
        dependent_points = self.sudoku.get_all_unit_points((row, col))
        for point in dependent_points:
            dependent_var = self.sudoku.get_variable_at_point(point)
            if dependent_var is not var:
                if dependent_var.value == val:
                    return False
        return True

    def order_domain_values(self, var):
        domain = list(var.domain)
        random.shuffle(domain)
        return domain

    # https://stackoverflow.com/questions/24343214/determine-whether-a-sudoku-has-a-unique-solution
    def solve(self, row, col, count):
        if row == 9:
            row = 0
            col += 1
            if col == 9:
                return count + 1
        
        if self.sudoku.grid[row][col].value != None:
            return self.solve(row + 1, col, count)
        
        for val in range(1, 10):
            if count < 2:
                if self.legal(row, col, val):
                    self.sudoku.grid[row][col].value = val
                    count = self.solve(row + 1, col, count)
        self.sudoku.grid[row][col].value = None
        return count

    def update_dependent_domains_after_reassignment(self, var):
        dependent_points = self.sudoku.get_all_unit_points(var.position)
        for point in dependent_points:
            dependent = self.sudoku.get_variable_at_point(point)
            dependent.domain.remove(var.value)

    def update_dependent_domains_before_deassignment(self, var):
        dependent_points = self.sudoku.get_all_unit_points(var.position)
        for point in dependent_points:
            dependent = self.sudoku.get_variable_at_point(point)
            dependent.domain.append(var.value)

    def write_puzzle(self):
        self.create_solution()
        self.backtrack_assignments({})


        return self.sudoku



