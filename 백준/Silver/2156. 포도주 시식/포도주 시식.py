import sys
n = int(sys.stdin.readline())

glass = []
dp = [0] * n

for i in range(n):
    glass.append(int(sys.stdin.readline()))

dp[0] = glass[0]

if n > 1:
    dp[1] = glass[0] + glass[1]
if n > 2:
    dp[2] = max(glass[2] + glass[0], glass[2] + glass[1], dp[1])
for j in range(3, n):
    dp[j]  = max(dp[j - 3] + glass[j - 1] + glass[j], dp[j - 2] + glass[j], dp[j - 1])

print(max(dp))