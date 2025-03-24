import sys

INF = int(1e9)

N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()

result = [INF, INF, INF]

for i in range(N):
    left = i
    mid = i + 1
    right = N - 1
    
    while mid < right:
        if abs(sum(result)) > abs(solutions[left] + solutions[mid] + solutions[right]):
            result = [solutions[left], solutions[mid], solutions[right]]

        if solutions[left] + solutions[mid] + solutions[right] == 0:
            result = [solutions[left], solutions[mid], solutions[right]]
            break
        elif solutions[left] + solutions[mid] + solutions[right] > 0:
            right -= 1
        else:
            mid += 1
    
print(*result)