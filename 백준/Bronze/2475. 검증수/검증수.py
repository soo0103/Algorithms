import sys

arr = list(map(int, sys.stdin.readline().split()))
value = 0

for i in range(len(arr)):
    value += arr[i] ** 2

print(value % 10)