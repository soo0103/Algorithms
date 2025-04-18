import sys

def get_multiplication(a, b):
    arr = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for k in range(N):
                arr[r][c] += a[r][k] * b[k][c]
            arr[r][c] %= 1000

    return arr

def get_square(matrix, B):
    if B == 1:
        for r in range(N):
            for c in range(N):
                matrix[r][c] %= 1000
        return matrix
    else:
        if B % 2 == 0:
            half_B = get_square(matrix, B // 2)
            return get_multiplication(half_B, half_B)
        else:
            half_B = get_square(matrix, (B - 1) // 2)
            return get_multiplication(get_multiplication(half_B, half_B), matrix)

if __name__ == "__main__":
    N, B = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    result = get_square(matrix, B)

    for r in result:
        print(*r)