import sys

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    A, B, C = map(int, sys.stdin.readline().split())

    if sum((A, B, C)) - max(A, B, C) <= max(A, B, C):
        print(f"Case #{i}: invalid!")
    else:
        if A == B == C:
            print(f"Case #{i}: equilateral")
        elif A == B or B == C or A == C:
            print(f"Case #{i}: isosceles")
        elif A != B and B != C and A != C:
            print(f"Case #{i}: scalene")