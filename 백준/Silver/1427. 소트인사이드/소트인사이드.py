import sys

num = int(sys.stdin.readline())
arr = list(map(int, str(num)))

arr.sort(reverse=True)

print(*arr, sep='')