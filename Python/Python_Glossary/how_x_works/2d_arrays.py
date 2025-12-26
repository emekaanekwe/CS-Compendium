'''
program that checks if a sudoku board is valid
'''
class Solution:
    def isValidSudoku(self, board) -> bool:
        #valid
        board = [["5","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
        #invalid
        '''
        board = [["8","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
        '''
        #test row validity
        for arr in board:
            new_row = []
            for row_item in arr:
                if row_item != '.':
                    new_row.append(int(row_item))
                row_set = set(new_row)
                if len(new_row) != len(row_set):
                    return False
        # column validity
        for count in range(len(board)):
            for arr in board:
                new_col = []
            if arr[count] != '.':
                new_col.append(int(arr[count]))
            else:
                continue
            col_set = set(new_col)
            print("col", new_col)
            if len(new_col) != len(col_set):
                return False
        #test 3x3 sub-box validity
        for row in range(len(board)): 
            first = 0
            new_grid = []        
            if row == 1:
                first = 0
            elif row == 2:
                first = 0
            elif row == 3:
                first = 3
            elif row == 4:
                first = 3          
            elif row == 5:          
                first = 3
            elif row == 6:          
                first = 6
            elif row == 7:          
                first = 6
            elif row == 8:          
                first = 6
            for count_one in range(3):
                second = 0
                if row == 1:
                    second = 3
                elif row == 2:
                    second = 6
                elif row == 3:
                    second = 0
                elif row == 4:
                    second = 3
                elif row == 5:          
                    second = 6
                elif row == 6:          
                    second = 0
                elif row == 7:          
                   second = 3
                elif row == 8:          
                    second = 6
                for count_two in range(3):
                    if board[first][second] != '.':
                        new_grid.append(int(board[first][second]))
                    second += 1
                first += 1
            grid_set = set(new_grid)
            if len(grid_set) != len(new_grid):
                return False
        return True
        