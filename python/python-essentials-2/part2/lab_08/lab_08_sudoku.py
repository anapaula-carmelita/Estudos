#  File name: lab_08_sudoku.py
#  Description: A possible solution for the 'LAB Sudoku' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-27
#  Version: 1.0
#  License: Apache
#

def isvalidsudoku(play):
    target = set('123456789')
    rows = play.splitlines()

    for row in rows:
        if set(row) != target:
            return "No"

    for c in range(9):
        col = ''.join(rows[r][c] for r in range(9))
        if set(col) != target:
            return "No"
    
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            block = []

            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    block.append(rows[r][c])
            if set(block) != target:
                return 'No'
    
    return 'Yes'
            
    
        


            



        
