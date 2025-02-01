import sys

N = int(sys.stdin.readline())

prev = N
cnt = 0

while 1:
    a = N // 10
    b = N % 10
    c = (a + b) % 10
    N = b * 10 + c
    cnt += 1
    if prev == N:
        break

print(cnt)