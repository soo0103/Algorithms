import sys

T = int(sys.stdin.readline())

if T % 10 != 0:
    print(-1)
else:
    A = T // 300
    B = (T % 300) // 60
    C = (T % 60) // 10

    print(A, B, C)