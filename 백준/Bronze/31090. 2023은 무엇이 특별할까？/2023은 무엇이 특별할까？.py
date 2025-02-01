import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    if (N + 1) % (N % 100) == 0:
        print("Good")
    else:
        print("Bye")