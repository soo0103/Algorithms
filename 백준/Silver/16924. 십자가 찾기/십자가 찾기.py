import sys
from copy import deepcopy

def getCross(r, c):
    global count
    cnt = 0

    for i in range(1, min(N, M)):
        if r + i < N and r - i >= 0 and c + i < M and c - i >= 0:
            if board[r + i][c] == board[r - i][c] == board[r][c - i] == board[r][c + i] == '*':
                cnt += 1
                copyBoard[r + i][c] = copyBoard[r - i][c] = copyBoard[r][c - i] = copyBoard[r][c + i] = copyBoard[r][c] = '.'
            else:
                break

    if cnt:
        count += cnt
        for j in range(1, cnt + 1):
            info.append((r + 1, c + 1, j))

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]

    copyBoard = deepcopy(board)
    count = 0
    info = []
    flag = True

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if board[i][j] == '*':
                getCross(i, j)

    for i in copyBoard:
        if '*' in i:
            flag = False
    
    if flag:
        info.sort(key = lambda x: (x[0], x[1], -x[2]))

        print(count)

        for x, y, s in info:
            print(x, y, s)
    else:
        print(-1)