import sys

N = sys.stdin.readline().strip()

if '0' not in N:
    print(-1)
else:
    num = 0

    for i in N:
        num += int(i)

    if num % 3 != 0:
        print(-1)
    else:
        print(''.join(sorted(N, reverse = True)))