import sys
n = int(sys.stdin.readline())

stairs = []
dp = [0] * n

for i in range(n):
    stairs.append(int(sys.stdin.readline()))

if n <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    for j in range(2, n):
        dp[j]  = max(dp[j - 3] + stairs[j - 1] + stairs[j], dp[j - 2] + stairs[j])

    print(dp[-1])