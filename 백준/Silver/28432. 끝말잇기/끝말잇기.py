import sys

N = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for _ in range(N)]

M = int(sys.stdin.readline())
A = [sys.stdin.readline().strip() for _ in range(M)]

i = S.index('?')

if i == 0:
    start = ''
else:
    start = S[i - 1][-1]

if i == len(S) - 1:
    end = ''
else:
    end = S[i + 1][0]

for a in A:
    if a not in S:
        if start == '' and end == '':
            print(a)
            break
        elif start == '' and a[-1] == end:
            print(a)
        elif end == '' and a[0] == start:
            print(a)
        elif a[0] == start and a[-1] == end:
            print(a)