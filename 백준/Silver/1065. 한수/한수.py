import sys

N = int(sys.stdin.readline())

result = 0

for i in range(1, N + 1):
    arr = list(map(int, str(i)))
    
    if i < 100:
        result += 1
    elif arr[1] - arr[0] == arr[2] - arr[1]:
        result += 1

print(result)