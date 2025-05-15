import sys

N, M = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort()

left = 0
right = 0
min_difference = A[-1] - A[0]

while right < N:
    difference = A[right] - A[left]

    if difference < M:
        right += 1
    elif difference > M:
        left += 1
        min_difference = min(min_difference, difference)
    else:
        min_difference = M
        break

print(min_difference)