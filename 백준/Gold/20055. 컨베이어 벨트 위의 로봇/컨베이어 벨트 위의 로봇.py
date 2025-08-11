import sys
from collections import deque

def rotate_belt():
    A.rotate(1)
    robots[-1] = False
    robots.rotate(1)
    robots[-1] = False
    
def move_robots():
    for i in range(N - 2, -1, -1):
        if A[i + 1] >= 1 and robots[i] and not robots[i + 1]:
            robots[i + 1] = True
            robots[i] = False
            A[i + 1] -= 1
    
    robots[-1] = False
            
def put_robot():
    if A[0] != 0 and not robots[0]:
        robots[0] = True
        A[0] -= 1

def check():
    cnt = 0
    
    for i in range(len(A)):
        if A[i] == 0:
            cnt += 1
    
    return cnt < K

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    A = deque(map(int, sys.stdin.readline().split()))

    robots = deque([False] * N)
    result = 0

    while check():
        result += 1
        rotate_belt()
        move_robots()
        put_robot()

    print(result)