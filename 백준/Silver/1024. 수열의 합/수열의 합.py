import sys

N, L = map(int, sys.stdin.readline().split())

for i in range(L, 101):
    x = N / i - (i + 1) / 2

    if int(x) == x:
        x = int(x)

        if x + 1 >= 0:
            for j in range(x + 1, x + i + 1):
                print(j, end=' ')
            break
else:
    print(-1)