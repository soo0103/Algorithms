import sys

def backtracking(cnt):
    if cnt == M:
        print(*seq)
        return
    for i in range(1, N + 1):
        seq[cnt] = i
        backtracking(cnt + 1)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    seq = [0] * M

    backtracking(0)