import sys

N = int(sys.stdin.readline())

for _ in range(N):
    if 6 <= len(sys.stdin.readline().strip()) <= 9:
        print("yes")
    else:
        print("no")