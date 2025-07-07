import sys

def backtracking(s):
    if len(s) == M:
        print(*s)
        return
    
    for i in range(len(arr)):
        s.append(arr[i])
        backtracking(s)
        s.pop()        

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = set(map(int, sys.stdin.readline().split()))

    arr = sorted(list(arr))
    seq = []

    backtracking(seq)