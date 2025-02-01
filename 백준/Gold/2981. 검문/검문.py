import sys
import math

N = int(sys.stdin.readline())
arr = []
div = []
factors = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for j in range(N - 1):
    value = arr[j + 1] - arr[j]
    div.append(value)

num = div[0]

for k in range(len(div) - 1):
    num = math.gcd(num, div[k + 1])

for l in range(2, int(num ** 0.5) + 1):
    if num % l == 0:
        factors.append(l)
        factors.append(num // l)

factors.append(num)
factors = list(set(factors))
factors.sort()

print(*factors, end=' ')