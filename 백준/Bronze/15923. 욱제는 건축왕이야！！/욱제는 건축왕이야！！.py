import sys

N = int(sys.stdin.readline())
coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

coordinates.append(coordinates[0])
perimeter = 0
prev = [coordinates[0][0], coordinates[0][1]]

for x, y in coordinates[1:]:
    perimeter += (abs(x - prev[0]) + abs(y - prev[1]))
    prev = [x, y]

print(perimeter)