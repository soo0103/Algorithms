import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

arr = sorted(A)
P = []

for i in range(N):
    P.append(arr.index(A[i]))
    arr[arr.index(A[i])] = -1

print(*P)