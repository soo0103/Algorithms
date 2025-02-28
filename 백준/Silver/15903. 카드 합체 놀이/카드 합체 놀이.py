import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    cards.sort()
    value = cards[0] + cards[1]
    cards[0] = value
    cards[1] = value

print(sum(cards))