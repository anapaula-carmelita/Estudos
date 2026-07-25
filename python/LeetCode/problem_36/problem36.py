class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        for i in range(9):
            numbers_in_row = {}
            numbers_in_col = {}
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in numbers_in_row:
                    numbers_in_row[board[i][j]] = 1
                elif board[i][j] != '.':
                    return False
                if board[j][i] != '.' and board[j][i] not in numbers_in_col:
                    numbers_in_col[board[j][i]] = 1
                elif board[j][i] != '.':
                    return False                                                                                                                                                                                                            
        for n1 in [0,3,6]:
            for n2 in [0,3,6]:
                numbers_in_part = {}
                for i in [0, 1, 2]:
                    for j in [0, 1, 2]:
                        if board[i+n1][j+n2] == '.':
                            continue
                        if board[i+n1][j+n2] not in numbers_in_part:
                            numbers_in_part[board[i+n1][j+n2]] = 1
                        else:
                            return False
        return True 