import sys

N, K = map(int, sys.stdin.readline().split())
nations = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

nations.sort(key = lambda x: (-x[1], -x[2], -x[3]))

prev = nations[0][1:]
rank = 1
cnt = 1

if N == 1 or (K == 1 and nations[0][0] == 1):
    print(1)
else:
    for i in range(1, N):
        if nations[i][1:] == prev:
            cnt += 1
        else:
            rank += cnt
            cnt = 1
            prev = nations[i][1:]

        if nations[i][0] == K:
            print(rank)
            break