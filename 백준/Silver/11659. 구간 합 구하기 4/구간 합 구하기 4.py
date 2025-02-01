import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefixSum = [0]
value = 0

for num in arr:
    value += num
    prefixSum.append(value)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefixSum[j] - prefixSum[i - 1])