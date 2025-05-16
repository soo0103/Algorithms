import sys
import heapq

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
heap = []

for num in nums:
    heapq.heappush(heap, num)

for i in range(N - 1):
    nums = list(map(int, sys.stdin.readline().split()))

    for num in nums:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])