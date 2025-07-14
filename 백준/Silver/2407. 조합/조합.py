import sys

def get_combination(n, r):
    if n == 1:
        return 1
    elif n == r or r == 0:
        return 1
    
    if dp[n][r] == 0:
        dp[n][r] = get_combination(n - 1, r) + get_combination(n - 1, r - 1)
    
    return dp[n][r]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    print(get_combination(n, m))