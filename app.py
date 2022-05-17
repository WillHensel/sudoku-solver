"""
This file is the main entry point to the Sudoku solver.
"""
import sys
from sudoku import *
from sudokusolveragent import *
from my_csv import *
from sudokuwriteragent import SudokuWriterAgent

def main():
    type = sys.argv[1]

    if type == 'solve':
        file_path = sys.argv[2]
        if file_path is None:
            print('Usage: python app.py solve <path_to_csv>')
            return
        initial_conditions = import_puzzle(file_path)
        game = Sudoku(initial_conditions)
        agent = SudokuSolverAgent(game)
        solved = agent.solve()
        if solved:
            game.print_grid()
            print('Valid?: ' + str(game.verify_validity()))
        else:
            print("Failed to solve")
            for i in range(9):
                for j in range(9):
                    print(game.grid[i][j].domain, end=' ')
                print()        
    elif type == 'write':
        agent = SudokuWriterAgent()
        game = agent.write_puzzle()
        game.print_grid()
        print('Valid?: ' + str(game.verify_validity()))
    else:
        print('Usage: python app.py <solve|write> <if solve: path_to_csv>')

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