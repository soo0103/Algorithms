import sys
from copy import deepcopy

def left(board):
    for r in range(N):
        col = 0
        for c in range(1, N):
            if board[r][c]:
                temp = board[r][c]
                board[r][c] = 0
                
                if board[r][col] == 0:
                    board[r][col] = temp
                elif board[r][col] == temp:
                    board[r][col] = 2 * temp
                    col += 1
                else:
                    col += 1
                    board[r][col] = temp
    return board

def right(board):
    for r in range(N):
        col = N - 1
        for c in range(N - 1, -1, -1):
            if board[r][c]:
                temp = board[r][c]
                board[r][c] = 0
                
                if board[r][col] == 0:
                    board[r][col] = temp
                elif board[r][col] == temp:
                    board[r][col] = 2 * temp
                    col -= 1
                else:
                    col -= 1
                    board[r][col] = temp
    return board

def up(board):
    for c in range(N):
        row = 0
        for r in range(1, N):
            if board[r][c]:
                temp = board[r][c]
                board[r][c] = 0
                
                if board[row][c] == 0:
                    board[row][c] = temp
                elif board[row][c] == temp:
                    board[row][c] = 2 * temp
                    row += 1
                else:
                    row += 1
                    board[row][c] = temp
    return board

def down(board):
    for c in range(N):
        row = N - 1
        for r in range(N - 1, -1, -1):
            if board[r][c]:
                temp = board[r][c]
                board[r][c] = 0
                
                if board[row][c] == 0:
                    board[row][c] = temp
                elif board[row][c] == temp:
                    board[row][c] = 2 * temp
                    row -= 1
                else:
                    row -= 1
                    board[row][c] = temp
    return board

def dfs(count, arr):
    global value
    if count == 5:
        for r in range(N):
            for c in range(N):
                if arr[r][c] > value:
                    value = arr[r][c]
        return value
    
    for i in range(4):
        new_board = deepcopy(arr)
        
        if i == 0:
            dfs(count + 1, left(new_board))
        elif i == 1:
            dfs(count + 1, right(new_board))
        elif i == 2:
            dfs(count + 1, up(new_board))
        else:
            dfs(count + 1, down(new_board))

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    value = 0
    board = []
    
    for _ in range(N):
        board.append(list(map(int ,sys.stdin.readline().split())))
        
    dfs(0, board)
    
    print(value)