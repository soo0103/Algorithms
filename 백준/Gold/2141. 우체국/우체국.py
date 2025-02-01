import sys

N = int(sys.stdin.readline())
village = []
people = 0
cnt = 0
post = 0

for _ in range(N):
    X, A = map(int, sys.stdin.readline().split())
    village.append((X, A))

village.sort(key = lambda x : x[0])

for i in village:
    people +=i[1]

mid = people // 2

if people % 2 != 0:
    mid += 1

for j in village:
    cnt += j[1]
    if cnt >= mid:
        print(j[0])
        break