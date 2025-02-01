import sys

H, M = map(int, sys.stdin.readline().split())

if M - 45 < 0:
    H -= 1
    M += 15
else:
    M -= 45

if M > 60:
    M -= 60
    H += 1

if H < 0:
    H += 24

print(H, M)