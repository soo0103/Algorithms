import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    print(f"{i}. {sys.stdin.readline().rstrip()}")