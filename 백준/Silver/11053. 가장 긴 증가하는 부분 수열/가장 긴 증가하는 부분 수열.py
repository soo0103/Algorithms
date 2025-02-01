import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))