import sys

INF = int(1e9)

N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()

result = [INF, INF]

left = 0
right = N - 1

while left < right:
    value = result[0] + result[1]
    comp = solutions[left] + solutions[right]

    if abs(value) > abs(comp):
        result = [solutions[left], solutions[right]]
    
    if comp == 0:
        result = [solutions[left], solutions[right]]
        break
    elif comp > 0:
        right -= 1
    else:
        left += 1
    
print(*result)