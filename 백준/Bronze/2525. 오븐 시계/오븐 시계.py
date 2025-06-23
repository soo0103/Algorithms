import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

hour = C // 60
minute = C % 60

B += minute

if B >= 60:
    B -= 60
    A += 1

A += hour

if A >= 24:
    A -= 24
    
print(A, B)