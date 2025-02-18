import sys
import heapq

N = int(sys.stdin.readline())
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lectures.sort()

classroom = []
heapq.heappush(classroom, lectures[0][1])

for i in range(1, N):
    if lectures[i][0] >= classroom[0]:
        heapq.heappop(classroom)
    heapq.heappush(classroom, lectures[i][1])

print(len(classroom))