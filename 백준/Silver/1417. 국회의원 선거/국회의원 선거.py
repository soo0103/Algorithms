import sys
import heapq

N = int(sys.stdin.readline())
nominees = [int(sys.stdin.readline()) for _ in range(N)]

dasom = nominees[0]
heap = []

if N == 1:
    print(0)
else:
    for i in range(1, N):
        heapq.heappush(heap, -nominees[i])

    while nominees[0] <= -min(heap):
        people = -heapq.heappop(heap)

        if nominees[0] <= people:
            people -= 1
            nominees[0] += 1
            heapq.heappush(heap, -people)

    print(nominees[0] - dasom)