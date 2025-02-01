import sys
from collections import deque

def right(num, dir):
    if num == 3:
        return
    if gear[num][2] != gear[num + 1][6]:
        right(num + 1, -dir)
        gear[num + 1].rotate(dir)

def left(num, dir):
    if num == 0:
        return
    if gear[num][6] != gear[num - 1][2]:
        left(num - 1, -dir)
        gear[num - 1].rotate(dir)

if __name__ == "__main__":
    gear = [deque(list(map(int, sys.stdin.readline().strip()))) for _ in range(4)]
    K = int(sys.stdin.readline())
    
    for i in range(K):
        num, dir = map(int, sys.stdin.readline().split())
        num -= 1
        right(num, -dir)
        left(num, -dir)
        gear[num].rotate(dir)

    score = 0
    
    for i in range(4):
        if gear[i][0] == 1:
            score += 2 ** i

    print(score)