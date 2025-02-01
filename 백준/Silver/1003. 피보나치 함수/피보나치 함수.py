import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    zero = [0] * (num + 1)
    one = [0] * (num + 1)
    zero[0] = 1

    if num != 0:
        zero[1] = 0
        one[1] = 1
    
    for i in range(2, num + 1):
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]
        
    print(zero[num], one[num])