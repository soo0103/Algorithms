import sys

N = int(sys.stdin.readline())
integers = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(integers.count(v))