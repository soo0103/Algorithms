import sys

N = int(sys.stdin.readline())
checkpoints = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

distance = [0]
MD = int(1e9)
dist = 0

for i in range(N - 1):
    d = abs(checkpoints[i + 1][0] - checkpoints[i][0]) + abs(checkpoints[i + 1][1] - checkpoints[i][1])
    distance.append(d)

total = sum(distance)

for i in range(1, N - 1):
    dist = total - distance[i + 1] - distance[i] + abs(checkpoints[i + 1][0] - checkpoints[i - 1][0]) + abs(checkpoints[i + 1][1] - checkpoints[i - 1][1])
    MD = min(MD, dist)

print(MD)