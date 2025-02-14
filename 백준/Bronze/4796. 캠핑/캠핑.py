import sys

i = 1

while 1:
    L, P, V = map(int, sys.stdin.readline().split())

    if L == P == V == 0:
        break

    cnt = V // P
    rest = V % P

    if L < rest:
        rest = L
    
    print(f"Case {i}: {L * cnt + rest}")

    i += 1