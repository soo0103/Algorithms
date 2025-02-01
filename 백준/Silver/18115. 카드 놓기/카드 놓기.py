import sys
from collections import deque

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.reverse()

dq = deque()

for i in range(N):
    if arr[i] == 1:
        dq.appendleft(i + 1)
    elif arr[i] == 2:
        dq.insert(1, i + 1)
    elif arr[i] == 3:
        dq.append(i + 1)

for i in dq:
    print(i, end=" ")