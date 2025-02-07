import sys

word = sys.stdin.readline().strip()

print((word == word[::-1]) * 1)