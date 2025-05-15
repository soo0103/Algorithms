import sys

N = map(int, sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

left = 0
right = len(A) - 1
min_solution = A[left] + A[right]

while left < right:
    solution = A[left] + A[right]

    if solution == 0:
        min_solution = 0
        break

    if abs(solution) < abs(min_solution):
        min_solution = solution

    if solution < 0:
        left += 1
    else:
        right -= 1

print(min_solution)