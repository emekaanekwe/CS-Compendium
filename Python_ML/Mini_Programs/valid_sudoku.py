'''
dual loop required 
valid row: take list and convert to set => check if list == set
valid col: same technique
valid grid: same technique
'''
from __future__ import annotations

    
b_valid=[   [0,0,0,3,5,0,9,0,1],
            [0,4,6,0,0,1,3,7,0],
            [0,0,0,8,0,4,0,0,0],
            [1,2,3,0,4,0,6,0,9],
            [7,0,5,4,3,2,1,0,0],
            [0,7,0,0,0,3,8,0,0],
            [6,0,0,0,1,7,9,0,5],
            [2,5,9,1,0,8,0,4,0],
            [4,0,0,7,5,0,2,0,8]
         ]
b_invalid=[ [0,0,0,3,5,0,9,0,1],
            [0,4,6,0,0,1,3,7,0],
            [0,0,0,8,0,4,0,0,0],
            [1,2,3,0,4,0,6,0,9],
            [7,0,5,4,3,2,1,0,0],
            [0,7,0,0,0,3,8,0,0],
            [6,0,0,0,1,7,9,0,5],
            [2,5,9,1,0,8,0,4,0],
            [4,0,0,7,5,0,2,0,8]
         ]

    
def validate_rows(board):
    for row in board:
        for num in row:
            print(num)

def validate_columns():
    return

def validate_grid():
    return

validate_rows(b_valid)