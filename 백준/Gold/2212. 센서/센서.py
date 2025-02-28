import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().split()))
sensors.sort()

distances = []

for i in range(N - 1):
    distances.append(sensors[i + 1] - sensors[i])

distances.sort()

print(sum(distances[:N - K]))