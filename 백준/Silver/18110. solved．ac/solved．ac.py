import sys

def roundup(n):
  if n - int(n) >= 0.5:
    return int(n) + 1
  else:
    return int(n)

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    arr = []

    for i in range(n):
        arr.append(int(sys.stdin.readline()))

    arr.sort()

    exc = roundup(n * 0.15)
    value = sum(arr)

    for j in range(exc):
        value -= arr[j]
        value -= arr[-1 - j]

    print(roundup(value / (n - 2 * exc)))