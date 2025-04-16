import sys

MAX_NUM = 123456 * 2 + 1

primes = [1] * MAX_NUM

for i in range(2, MAX_NUM):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            primes[i] = 0
            break

while 1:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    print(sum(primes[n + 1: 2 * n + 1]))