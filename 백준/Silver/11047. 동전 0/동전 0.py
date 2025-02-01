import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
cnt = 0

for i in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse = True)

for coin in coins:
    cnt += K // coin
    K %= coin
    if K == 0:
        break

print(cnt)