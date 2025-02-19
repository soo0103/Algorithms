import sys

PI = 3.14159265358979

A1, P1 = map(int, sys.stdin.readline().split())
R1, P2 = map(int, sys.stdin.readline().split())

A2 = R1 * R1 * PI

if A1 / P1 > A2 / P2:
    print("Slice of pizza")
else:
    print("Whole pizza")