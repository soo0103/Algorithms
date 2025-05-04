import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

seq.sort()

start = 0
end = len(seq) - 1
cnt = 0

while start < end:
    a = seq[start] + seq[end]

    if a == x:
        cnt += 1
        start += 1
    elif a < x:
        start += 1
    else:
        end -= 1

print(cnt)