import sys

def recursion(r, c, s):
    if s == 3:
        stars[r][c] = '*'
        stars[r + 1][c - 1] = stars[r + 1][c + 1] = '*'

        for i in range(-2, 3):
            stars[r + 2][c - i] = '*'
    
    else:
        size = s // 2
        recursion(r, c, size)
        recursion(r + size, c - size, size)
        recursion(r + size, c + size, size)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    stars = [[' '] * (2 * N) for _ in range(N)]

    recursion(0, N - 1, N)

    for star in stars:
        print("".join(star))