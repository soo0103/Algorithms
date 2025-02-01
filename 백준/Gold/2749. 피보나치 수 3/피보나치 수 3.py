import sys

n = int(sys.stdin.readline())

M = 1000000
P = 15 * (10 ** 5)

fib = [0] * (P + 1)
fib[1] = 1

for i in range(2, P + 1):
    fib[i] = (fib[i - 1] + fib[i - 2]) % M

print(fib[n % P])