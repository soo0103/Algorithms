import sys

N = int(sys.stdin.readline())
logs = list(map(int, sys.stdin.readline().split()))

dic = {}
cnt = 0

for log in logs:
    if log > 0:
        dic[log] = 1
    else:
        if -log in dic:
            dic[-log] -1
        else:
            cnt += 1

print(cnt)