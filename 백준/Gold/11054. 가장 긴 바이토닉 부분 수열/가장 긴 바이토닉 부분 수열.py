import sys

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))

left = [1] * N
right = [1] * N
cnt = 0

for i in range(N):
    for j in range(i):
        if S[i] > S[j]:
            left[i] = max(left[i], left[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if S[i] > S[j]:
            right[i] = max(right[i], right[j] + 1)

for i in range(N):
    cnt = max(cnt, right[i] + left[i] - 1)

print(cnt)