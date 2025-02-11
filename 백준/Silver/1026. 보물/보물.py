import sys

N = int(sys.stdin.readline())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0

for i in range(N):
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(S)