import sys

N, L = map(int, sys.stdin.readline().split())
location = list(map(int, sys.stdin.readline().split()))
location.sort()

start = location[0]
cnt = 1

for l in location[1:]:
    if l not in range(start, start + L):
        start = l
        cnt += 1

print(cnt)