import sys

N = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().split()))

print(*sorted(arr))