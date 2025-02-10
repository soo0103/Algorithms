import sys

a = sys.stdin.readline().strip()

print(bin(int(a, 8))[2:])