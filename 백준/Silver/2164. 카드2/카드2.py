import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque([i + 1 for i in range(N)])

while len(dq) != 1:
        dq.popleft()
        num = dq.popleft()
        dq.append(num)

print(dq[0])