import sys

w, h = map(int, sys.stdin.readline().split())

d = (w ** 2 + h ** 2) ** 0.5

print(w + h - d)