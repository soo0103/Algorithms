import sys

n, k = map(int, sys.stdin.readline().split())
arr = [[0] * n for _ in range(n)]

if n >= 1:
    arr[0][0] = 1

if n >= 2:
    arr[1][0] = 1
    arr[1][1] = 1

for l in range(2, n):
    arr[l][0] = 1 
    
    for m in range(n):
        arr[l][m] = arr[l - 1][m] + arr[l - 1][m - 1]

print(arr[n - 1][k - 1])