import sys

N = int(sys.stdin.readline())
room = [list(sys.stdin.readline().strip()) for _ in range(N)]

w = 0
l = 0

for r in range(N):
    tmp1 = 0
    tmp2 = 0

    for c in range(N):
        if room[r][c] == '.':
            tmp1 += 1
        else:
            tmp1 = 0

        if tmp1 == 2:
            w += 1

        if room[c][r] == '.':
            tmp2 += 1
        else:
            tmp2 = 0

        if tmp2 == 2:
            l +=1

print(w, l)