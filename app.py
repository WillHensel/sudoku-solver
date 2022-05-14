"""
This file is the main entry point to the Sudoku solver.
"""
from sudoku import *
from sudokuagent import *
from my_csv import *

def main():
    initial_conditions = import_puzzle("test_puzzles/hard_puzzle_1.csv")
    game = Sudoku(initial_conditions)
    agent = SudokuAgent(game)
    solved = agent.solve()
    if solved:
        game.print_grid()
    else:
        print("Failed to solve")
        for i in range(9):
            for j in range(9):
                print(game.grid[i][j].domain, end=' ')
            print()

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