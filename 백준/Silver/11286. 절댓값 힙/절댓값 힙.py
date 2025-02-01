import sys
import heapq

N = int(sys.stdin.readline())

abs_heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(abs_heap, (abs(num), num))
    else:
        if not abs_heap:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])