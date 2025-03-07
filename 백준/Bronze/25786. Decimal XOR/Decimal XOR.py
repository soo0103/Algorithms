import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

if len(A) < len(B):
    A = '0' * (len(B) - len(A)) + A
else:
    B = '0' * (len(A) - len(B)) + B

result = ''

for i in range(len(A)):
    if (A[i] <= '2' and B[i] <= '2') or (A[i] >= '7' and B[i] >= '7'):
        result += '0'
    else:
        result += '9'

print(result)