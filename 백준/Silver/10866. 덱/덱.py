import sys

deque = []

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()
    cmd = command[0]

    if len(command) == 2:
        num = command[1]

    if cmd == "push_front":
        deque.insert(0, num)
    elif cmd == "push_back":
        deque.append(num)
    elif cmd == "pop_front":
        if deque:
            print(deque[0])
            deque.remove(deque[0])
        else:
            print(-1)
    elif cmd == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(deque))
    elif cmd == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)