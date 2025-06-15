import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
location = list(map(int, sys.stdin.readline().split()))

arr = deque([x for x in range(1, N + 1)])
cnt = 0

for i in location:
    while 1:
        if arr[0] == i:
            arr.popleft()
            break
        else:
            if arr.index(i) <= len(arr) // 2:
                arr.rotate(-1)
                cnt += 1
            else:
                arr.rotate(1)
                cnt += 1
                
print(cnt)