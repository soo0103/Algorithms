import sys

N = int(sys.stdin.readline())

num = 11
cnt = 1

while N >= num:
    num = num * 10 + 1
    cnt += 1

print(cnt)