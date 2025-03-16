import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
cnt = 0
result = A[0]

while 1:
    if result < M:
        end += 1
        if end >= N:
            break
        result += A[end]
    else:
        if result == M:
            cnt += 1
        result -= A[start]
        start += 1

print(cnt)