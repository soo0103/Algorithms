import sys

T = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * 80001
tmp = 0

for i in range(1, 80001):
    if i % 3 == 0 or i % 7 == 0:
        tmp += i
    dp[i] += tmp

for num in arr:
    print(dp[num])