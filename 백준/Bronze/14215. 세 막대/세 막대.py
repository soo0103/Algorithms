import sys

arr = sorted(list(map(int, sys.stdin.readline().split())))

if arr[0] + arr[1] > arr[2]:
    print(sum(arr))
else:
    print((arr[0] + arr[1]) * 2 - 1)