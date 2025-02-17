import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

height = [0] * N

for i in range(N):
    cnt = 0

    for j in range(N):
        if line[i] == cnt and not height[j]:
            height[j] = i + 1
            break
        elif not height[j]:
            cnt += 1

print(*height)