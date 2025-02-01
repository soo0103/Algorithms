import sys

N, X = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

for num in arr:
    if num < X:
        print(num, end= " ")