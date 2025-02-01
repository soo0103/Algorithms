import sys

x, y, w, h = map(int, sys.stdin.readline().split())

left = x
right = w - x
up = h - y
down = y

print(min(left, right, up, down))