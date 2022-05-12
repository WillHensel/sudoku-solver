"""
This file is the main entry point to the Sudoku solver.
"""
from sudoku import *
from sudokuagent import *

def main():
    initialConditions = [
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

    game = Sudoku(initialConditions)
    agent = AC3Agent(game)
    solved = agent.ac_3()
    print(solved)
    print(game.grid)

if __name__ == "__main__":
    main()