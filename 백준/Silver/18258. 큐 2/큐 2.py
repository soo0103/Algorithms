import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    cmd = command[0]

    if len(command) == 2:
        num = command[1]

    if cmd == "push":
        queue.append(num)
    elif cmd == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)