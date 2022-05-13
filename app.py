"""
This file is the main entry point to the Sudoku solver.
"""
from sudoku import *
from sudokuagent import *
from my_csv import *

def main():
    initial_conditions = import_puzzle("test_puzzles/medium_puzzle_1.csv")
    game = Sudoku(initial_conditions)
    agent = SudokuAgent(game)
    solved = agent.solve()
    if solved:
        print("Success!")
        for i in range(9):
            if i != 0 and i % 3 == 0:
                print(str('-') * 7 * 3)
            for j in range(9):
                if j != 0 and j % 3 == 0:
                    print('|', end=' ')
                print(game.grid[i][j][0], end=' ')
            print()
    else:
        print("Failed to solve")
        for i in range(9):
            print(game.grid[i])

def import_puzzle(file):
    csv = CSV(file)
    array = csv.read()
    initial_conditions = []
    for i in range(9):
        for j in range(9):
            val =  int(array[i][j])
            if val != 0:
                initial_conditions.append(((i, j), val))
    return initial_conditions


if __name__ == "__main__":
    main()