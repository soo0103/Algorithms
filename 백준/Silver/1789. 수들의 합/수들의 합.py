import sys

S = int(sys.stdin.readline())

i = 0
cnt = 0

while S > i:
    i += 1
    S -= i
    cnt += 1

print(cnt)