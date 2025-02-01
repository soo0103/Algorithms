import sys

equation = sys.stdin.readline().split('-')
arr = []

for i in equation:
    sum = 0
    num = i.split('+')

    for j in num:
        sum += int(j)

    arr.append(sum)

value = arr[0]

for j in range(1, len(arr)):
    value -= arr[j]
    
print(value)