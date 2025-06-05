import sys

A = int(sys.stdin.readline())
B = sys.stdin.readline().strip()[::-1]

result = 0

for i in range(len(B)):
    tmp = A * int(B[i])
    result += tmp * (10 ** i)
    print(tmp)

print(result)