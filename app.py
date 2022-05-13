"""
This file is the main entry point to the Sudoku solver.
"""
from sudoku import *
from sudokuagent import *

def main():
    initialConditions = [
        ((0, 1), 7), ((0, 2), 1), ((0, 4), 6), ((0, 5), 9), ((0, 6), 5),
        ((1, 2), 9), ((1, 6), 6),
        ((2, 2), 6), ((2, 3), 7), ((2, 7), 9),
        ((3, 1), 9), ((3, 2), 8), ((3, 5), 7), ((3, 6), 2), ((3, 7), 6),
        ((4, 0), 1), ((4, 1), 3), ((4, 2), 2), ((4, 3), 8), ((4, 7), 7), ((4, 8), 4),
        ((5, 2), 4), ((5, 3), 1), ((5, 4), 9), ((5, 5), 2), ((5, 6), 8), ((5, 7), 3),
        ((6, 2), 7), ((6, 4), 8),
        ((7, 0), 9), ((7, 1), 1), ((7, 3), 4), ((7, 5), 3), ((7, 6), 7), ((7, 7), 8),
        ((8, 1), 8), ((8, 5), 1), ((8, 8), 2),
    ]

    game = Sudoku(initialConditions)
    print('Before')
    for i in range(9):
        print(game.grid[i])
    agent = AC3Agent(game)
    solved = agent.ac_3()
    print('After')
    for i in range(9):
        print(game.grid[i])

if __name__ == "__main__":
    main()