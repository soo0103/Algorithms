import sys

def flip(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if A[i][j]:
                A[i][j] = 0
            else:
                A[i][j] = 1

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    A = [list(map(int, str(sys.stdin.readline()).strip())) for _ in range(N)]
    B = [list(map(int, str(sys.stdin.readline()).strip())) for _ in range(N)]

    cnt = 0

    if (N < 3 or M < 3) and A != B:
        print(-1)
    else:
        for i in range(N - 2):
            for j in range(M - 2):
                if A[i][j] != B[i][j]:
                    flip(i, j)
                    cnt += 1

        if A != B:
            print(-1)
        else:
            print(cnt)