import sys
from collections import defaultdict

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

sum_A = defaultdict(int)
cnt = 0

for i in range(n):
    for j in range(i + 1, n + 1):
        sum_A[sum(A[i:j])] += 1

for i in range(m):
    for j in range(i + 1, m + 1):
        cnt += sum_A[T - sum(B[i:j])]

print(cnt)