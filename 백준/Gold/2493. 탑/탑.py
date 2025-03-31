import sys

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

received = [0] * N
s = []

for i in range(N):
    while s:
        if s[-1][1] > towers[i]:
            received[i] = s[-1][0] + 1
            break
        else:
            s.pop()
    s.append((i, towers[i]))

print(*received)