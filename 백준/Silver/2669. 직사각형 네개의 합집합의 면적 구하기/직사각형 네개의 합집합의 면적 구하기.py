import sys

squares = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
coordinates = [[0] * 101 for _ in range(101)]

result = 0

for x1, y1, x2, y2 in squares:
    for r in range(y1, y2):
        for c in range(x1, x2):
            if coordinates[r][c] == 1:
                continue
            else:
                coordinates[r][c] = 1
                result += 1

print(result)