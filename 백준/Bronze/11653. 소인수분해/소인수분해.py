import sys

N = int(sys.stdin.readline())

if N == 1:
    print('')
else:
    for i in range(2, N + 1):
        if N % i == 0:
            while N % i == 0:
                print(i)
                N = N // i