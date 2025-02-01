import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

arr = [0] * 10
s = str(A * B * C)

for i in s:
    arr[int(i)] += 1

print(*arr, sep='\n')