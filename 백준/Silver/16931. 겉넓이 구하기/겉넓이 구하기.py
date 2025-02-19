import sys

N, M = map(int, sys.stdin.readline().split())
cubes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

area = 0

for i in range(N):
    area += cubes[i][0]
    area += cubes[i][-1]

    for j in range(1, M):
        area += abs(cubes[i][j] - cubes[i][j - 1])

for i in range(M):
    area += cubes[0][i]
    area += cubes[-1][i]

    for j in range(1, N):
        area += abs(cubes[j][i] - cubes[j - 1][i])

area += 2 * M * N

print(area)
