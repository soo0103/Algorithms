import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)
for i in range(2, N + 1):
    
    dp[i] = dp[i - 1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

result = [N]
current = N
value = dp[N] - 1

for i in range(N, 0, -1):
    if dp[i] == value and (i + 1 == current or i * 2 == current or i * 3 == current):
        current = i
        result.append(i)
        value -= 1

print(dp[N])
print(*result)