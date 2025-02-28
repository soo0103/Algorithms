import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))

    profit = 0
    price = 0

    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > price:
            price = prices[i]
        else:
            profit += price - prices[i]
    
    print(profit)