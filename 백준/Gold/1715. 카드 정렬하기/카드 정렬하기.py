import sys
import heapq

N = int(sys.stdin.readline())

cards = []

for i in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

total = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_value = a + b
    
    total += sum_value
    heapq.heappush(cards, sum_value)

print(total)