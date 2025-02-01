import sys

N = int(sys.stdin.readline())

if N == 1:
    print(3)
else:
    lion = [0] * N
    lion[0] = 3
    lion[1] = 7

    for i in range(2, N):
        lion[i] = (2 * lion[i - 1] + lion[i - 2]) % 9901
    
    print(lion[N - 1])