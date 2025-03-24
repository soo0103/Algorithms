import sys

INF = int(1e9)

def find_solutions():
    global result
    for i in range(N - 2):
        left = i
        mid = i + 1
        right = N - 1
        
        while mid < right:
            value = result[0] + result[1] + result[2]
            comp = solutions[left] + solutions[mid] + solutions[right]
            
            if abs(value) > abs(comp):
                result = [solutions[left], solutions[mid], solutions[right]]

            if comp == 0:
                result = [solutions[left], solutions[mid], solutions[right]]
                return
            elif comp > 0:
                right -= 1
            else:
                mid += 1

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    solutions = list(map(int, sys.stdin.readline().split()))
    solutions.sort()

    result = [INF, INF, INF]

    find_solutions()
        
    print(*result)