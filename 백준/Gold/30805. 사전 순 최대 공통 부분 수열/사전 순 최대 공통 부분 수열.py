import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

common_arr = set(A) & set(B)
seq = []

while common_arr:
    max_num = max(common_arr)
    seq.append(max_num)
    
    i1 = A.index(max_num)
    i2 = B.index(max_num)

    A = A[i1 + 1:]
    B = B[i2 + 1:]

    common_arr = set(A) & set(B)
    
print(len(seq))
print(*seq)