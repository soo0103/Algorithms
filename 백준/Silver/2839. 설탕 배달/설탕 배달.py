import sys

N = int(sys.stdin.readline())

cnt = 0

while 1:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    elif N % 5 != 0:
        N -= 3
        cnt += 1

    if N < 0:
        print(-1)
        break