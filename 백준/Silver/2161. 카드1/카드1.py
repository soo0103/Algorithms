import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque(list(i for i in range(1, N + 1)))

result = []

while dq:
    result.append(dq.popleft())
    if dq:
        dq.append(dq.popleft())

print(*result)