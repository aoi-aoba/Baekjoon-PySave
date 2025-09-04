import sys
SIZE = 9
BOX_SIZE = 3

board = [list(map(int, sys.stdin.readline().split())) for _ in range(SIZE)]
cellToSee = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]

def sudoku(n):
    if n == len(cellToSee):
        print('\n'.join(' '.join(str(j) for j in board[i]) for i in range(9)))
        exit()
    for check_num in range(1, 10):
        row, col = cellToSee[n]
        if check(row, col, check_num):
            board[row][col] = check_num
            sudoku(n + 1)
            board[row][col] = 0

def check(row, col, num):
    for cellIdx in range(SIZE):
        if board[row][cellIdx] == num or board[cellIdx][col] == num:
            return False
    for r in range(BOX_SIZE):
        for c in range(BOX_SIZE):
            if num == board[row // BOX_SIZE * BOX_SIZE + r][col // BOX_SIZE * BOX_SIZE + c]:
                return False
    return True

sudoku(0)