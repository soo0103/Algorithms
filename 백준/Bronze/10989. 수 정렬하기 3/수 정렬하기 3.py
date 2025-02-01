import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(N):
    arr[int(sys.stdin.readline())] += 1
    
for j in range(1, len(arr)):
    for k in range(arr[j]):
        print(j)