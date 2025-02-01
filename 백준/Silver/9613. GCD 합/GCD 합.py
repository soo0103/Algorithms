import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    value = 0
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            value += math.gcd(arr[i], arr[j])
    
    print(value)