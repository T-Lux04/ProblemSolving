board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

def isValidSudoku(board, row, col, num):
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                num = board[i][j]
                if num in board[row]:
                    return False
                
                for i in range(9):
                    if num == board[i][col]:
                        return False
                start_row = row - row % 3
                start_col = col - col % 3
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if num == board[i][j]:
                            return False
                return True





if isValidSudoku( board, i, j, num):
    print("Valid!!!")
else:
    print("Invalid!!")

    
    
    