import sys

N = int(sys.stdin.readline())
mirror = [list(sys.stdin.readline().strip()) for _ in range(N)]
K = int(sys.stdin.readline())

if K == 1:
    for i in mirror:
        print(*i, sep = '')
elif K == 2:
    for i in mirror:
        print(*i[::-1], sep = '')
else:
    for i in reversed(mirror):
        print(*i, sep = '')