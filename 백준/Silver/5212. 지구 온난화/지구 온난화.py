import sys
import copy

R, C = map(int, sys.stdin.readline().split())
map = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x1 = y1 = x2 = y2 = 0

for _ in range(R):
    map.append(list(input()))

answer = copy.deepcopy(map)

for y in range(R):
    for x in range(C):
        if map[y][x] == 'X':
            cnt = 0

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < C and 0 <= ny < R:
                    if map[ny][nx] == '.':
                        cnt += 1
                else:
                    cnt += 1

            if cnt >= 3:
                answer[y][x] = '.'

x1 = 0
y1 = C - 1
x2 = 0
y2 = 0

for i in range(0, R):
    if 'X' in answer[i]:
        x1 = i
        break

for i in range(R - 1, -1, -1):
    if 'X' in answer[i]:
        x2 = i
        break

for i in range(x1, x2 + 1):
    for j in range(C):
        if answer[i][j] == 'X':
            y1 = min(y1, j)
            y2 = max(y2, j)

for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        print(answer[i][j], end='')
    print()