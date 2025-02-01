import sys

N = int(sys.stdin.readline())
time = []

for i in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key = lambda x : (x[1], x[0]))
cnt = 1
endtime = time[0][1]

for j in range(1, N):
    if time[j][0] >= endtime:
        cnt += 1
        endtime = time[j][1]

print(cnt)