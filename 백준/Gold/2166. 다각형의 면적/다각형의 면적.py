import sys

N = int(sys.stdin.readline())
coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
coordinates.append(coordinates[0])
area = 0

for i in range(N):
    area += coordinates[i][0] * coordinates[i + 1][1] - coordinates[i + 1][0] * coordinates[i][1]

print(abs(area) / 2)