import sys

x, y = map(int, sys.stdin.readline().split())

x_arr = [0, x] 
y_arr = [0, y] 

for _ in range(int(input())):
    dir, length = map(int, sys.stdin.readline().split())
    
    if dir == 0:
        y_arr.append(length)
    else:
        x_arr.append(length)
        
x_arr.sort() 
y_arr.sort()

result = 0

for i in range(1, len(x_arr)):
    for j in range(1, len(y_arr)):
        width = x_arr[i] - x_arr[i - 1]
        height = y_arr[j] - y_arr[j - 1]

        result = max(result, width * height) 

print(result)