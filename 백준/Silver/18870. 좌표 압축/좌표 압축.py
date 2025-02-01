import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
zipped = {}
sorted_arr = sorted(set(arr))

for i in range(len(sorted_arr)):
    zipped[sorted_arr[i]] = i

for i in arr:
    print(zipped[i], end=' ')