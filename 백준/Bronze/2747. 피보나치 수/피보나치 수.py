import sys

n = int(sys.stdin.readline())

fib = [0] * (n + 1)

if n >= 1:
    fib[1] = 1

if n >= 2:
    fib[2] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

print(fib[n])