import sys

def backtracking(s):
    if len(s) == M:
        print(*s)
        return
    
    for i in range(N):
        s.append(arr[i])
        backtracking(s)
        s.pop()        

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()
    seq = []

    backtracking(seq)