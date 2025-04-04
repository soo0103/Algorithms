import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j] + 1, dp[i])

length = max(dp)
arr = []

for i in range(N - 1, -1, -1):
    if dp[i] == length:
        arr.append(A[i])
        length -= 1

print(max(dp))
print(*reversed(arr))