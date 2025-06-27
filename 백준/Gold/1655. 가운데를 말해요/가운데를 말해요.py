import sys
import heapq

N = int(sys.stdin.readline())

left = []
right = []

for i in range(N):
    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and right[0] < -left[0]:
        left_num = heapq.heappop(left)
        right_num = heapq.heappop(right)

        heapq.heappush(left, -right_num)
        heapq.heappush(right, -left_num)

    print(-left[0])