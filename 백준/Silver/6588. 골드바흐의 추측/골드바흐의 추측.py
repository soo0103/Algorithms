import sys

arr = [1] * 1000001

for i in range(2, int(len(arr) ** 0.5) + 1):
    if arr[i]:
        for j in range(2 * i, 1000001, i):
            arr[j] = 0

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in range(n - 3, 2, -2):
        if (arr[i] == 1) and (arr[n - i] == 1):
            print(f"{n} = {n - i} + {i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')