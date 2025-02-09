import sys

T = int(sys.stdin.readline())

for _ in range(T):
    sentence = list(sys.stdin.readline().split())

    for s in sentence:
        print(s[::-1], end = " ")