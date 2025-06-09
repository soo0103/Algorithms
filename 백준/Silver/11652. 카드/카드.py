import sys

N = int(sys.stdin.readline())
cards = {}

for _ in range(N) :
    card = int(sys.stdin.readline())
    
    if card in cards:
        cards[card] += 1
    else :
        cards[card] = 1

result = sorted(cards.items(), key = lambda x : (-x[1], x[0]))

print(result[0][0])