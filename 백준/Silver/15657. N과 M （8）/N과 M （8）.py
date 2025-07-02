import sys

def backtracking(s):
    if len(s) == M:
        print(*s)
        return
    
    for num in arr:
        if not s or s[-1] <= num:
            s.append(num)
            backtracking(s)
            s.pop()

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()

    seq = []

    backtracking(seq)