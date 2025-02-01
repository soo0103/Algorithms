import sys
import copy

R, C, N = map(int, sys.stdin.readline().split())
bomb = []
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
splash = []

for _ in range(R):
    bomb.append(list(input()))

for i in range(0, N + 1):
    if i == 0:
        splash = copy.deepcopy(bomb)
        continue

    if i == 1:
        continue
    elif i % 2 == 0:
        splash = [['O'] * C for _ in range(R)]
    elif i % 2 == 1:
        for k in range(R):
            for l in range(C):
                if bomb[k][l] == 'O':
                    splash[k][l] = '.'

                    for m in range(4):
                        nx = l + dx[m]
                        ny = k + dy[m]

                        if 0 <= nx < C and 0 <= ny < R:
                            splash[ny][nx] = '.'

        bomb = copy.deepcopy(splash)
        
for o in range(R):
    print(*splash[o], sep='')