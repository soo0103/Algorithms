import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, N + 1)])
result = []

while len(dq) != 0:
    for _ in range(K - 1):
        dq.append(dq.popleft())

    result.append(str(dq.popleft()))
    
print('<' + ', '.join(result) + '>')