import sys

N, M = map(int, sys.stdin.readline().split())
distance = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

coordinates = []

for r in range(N):
    for c in range(M):
        if distance[r][c] == 1:
            coordinates.append([r, c])

D = abs(coordinates[1][0] - coordinates[0][0]) + abs(coordinates[1][1] - coordinates[0][1])

print(D)