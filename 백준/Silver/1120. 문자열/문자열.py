import sys

A, B = sys.stdin.readline().split()

result = int(1e9)

for i in range(len(B) - len(A) + 1):
    cnt = 0

    for j in range(len(A)):
        if A[j] != B[j + i]:
            cnt += 1

    result = min(result, cnt)

print(result)