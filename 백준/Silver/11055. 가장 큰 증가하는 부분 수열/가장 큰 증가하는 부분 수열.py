import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
for i in range(N):
    dp[i] = A[i]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j] + A[i], dp[i])

print(max(dp))