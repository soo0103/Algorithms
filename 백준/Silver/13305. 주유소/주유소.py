import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

value = price[0]
cost = 0

for i in range(N - 1):
    value = min(value, price[i])
    cost += value * road[i]

print(cost)