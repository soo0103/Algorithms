import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a + b + c == 180:
    if a == 60 and b == 60 and c == 60:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    elif a != b and b != c and c != a:
        print("Scalene")
else:
    print("Error")