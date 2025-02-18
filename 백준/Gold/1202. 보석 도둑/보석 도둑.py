import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewelry = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]

jewelry.sort(key = lambda x: -x[0])
bags.sort()

heap = []
value = 0

for bag in bags:
    while jewelry:
        M, V = jewelry.pop()
        
        if bag >= M:
            heapq.heappush(heap, -V)
        else:
            jewelry.append([M, V])
            break
    
    if heap:
        value -= heapq.heappop(heap)

print(value)