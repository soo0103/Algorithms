import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

NGE = [-1] * N
stack = [0]

for i in range(N):
    while stack and seq[stack[-1]] < seq[i]:
        NGE[stack.pop()] = seq[i]

    stack.append(i)

print(*NGE)