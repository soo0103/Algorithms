import sys

M = int(sys.stdin.readline())

S = set()

for _ in range(M):
    command = list(map(str, sys.stdin.readline().split()))
    cmd = command[0]

    if len(command) == 2:
        n = int(command[1])
    
    if cmd == "add":
        S.add(n)
    elif cmd == "remove":
        if n in S:
            S.remove(n)
    elif cmd == "check":
        if n in S:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    elif cmd == "all":
        S = set([i for i in range(1, 21)])
    elif cmd == "empty":
        S = set()