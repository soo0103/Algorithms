import sys

PI = 3.1415926535

H = int(sys.stdin.readline()) * 100
W = int(sys.stdin.readline()) * 100

print(min(H, W) // 2)