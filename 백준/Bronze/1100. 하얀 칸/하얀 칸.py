import sys

board = [list(sys.stdin.readline().strip()) for _ in range(8)]

cnt = 0

for r in range(8):
    for c in range(8):
        if (r + c) % 2 == 0 and board[r][c] == 'F':
            cnt += 1

print(cnt)