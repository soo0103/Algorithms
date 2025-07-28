import sys

def check(row, col, x):
    for i in range(9):
        if x == board[row][i]:
            return False
 
    for j in range(9):
        if x == board[j][col]:
            return False

    for r in range(3):
        for c in range(3):
            if x == board[row // 3 * 3 + r][col // 3 * 3 + c]:
                return False
    
    return True

def backtracking(cnt):
    if cnt == blank_count:
        for row in board:
            print(*row)
        
        exit(0)

    for n in range(1, 10):
        r, c = blank[cnt]

        if check(r, c, n):
            board[r][c] = n
            backtracking(cnt + 1)
            board[r][c] = 0

if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    blank = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blank.append((i, j))
    
    blank_count = len(blank)

    backtracking(0)