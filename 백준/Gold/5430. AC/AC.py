import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    cmd = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    flag = 0
    rev = 0

    if N == 0:
        arr = deque()

    for j in cmd:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(arr) == 0:
                print("error")
                flag = 1
                break
            else:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if not flag:
        if rev % 2 == 0:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')