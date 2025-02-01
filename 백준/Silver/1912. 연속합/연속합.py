import sys

n = int(sys.stdin.readline())
dp = list(map(int, sys.stdin.readline().split()))
 
for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + dp[i - 1])
    
print(max(dp))