import sys

arr = []
total = 0

for i in range(10):
    arr.append(int(sys.stdin.readline()))

for j in range(10):
    total += arr[j]

    if total >= 100:
        if total - 100 > 100 - (total - arr[j]):
            total -= arr[j]
            break

print(total)