import random
import time

from sudoku import *
from sudokusolveragent import *

class SudokuWriterAgent:

    def __init__(self):
        random.seed = time.time()
        self.sudoku = Sudoku([])

    def order_domain_values(self, var):
        domain = list(var.domain)
        random.shuffle(domain)
        return domain

    def write_puzzle(self):
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
        return self.sudoku



