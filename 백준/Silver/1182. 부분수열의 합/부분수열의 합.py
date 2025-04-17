import sys
sys.setrecursionlimit(10 ** 6)

def backtracking(start):
    global cnt
    if sum(arr) == S and len(arr) > 0:
        cnt += 1

    for i in range(start, N):
        arr.append(seq[i])
        backtracking(i + 1)
        arr.pop()

if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    seq = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    arr = []

    backtracking(0)

    print(cnt)