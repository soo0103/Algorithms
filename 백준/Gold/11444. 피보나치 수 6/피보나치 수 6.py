import sys
sys.setrecursionlimit(10 ** 6)

MOD = 1000000007

def fib(x):
    if x not in dp:
        k = x // 2
        if x % 2 == 0:
            dp[x] = (fib(k) * (fib(k) + 2 * fib(k - 1))) % MOD
        else:
            dp[x] = (fib(k) ** 2 + fib(k + 1) ** 2) % MOD
    return dp[x]
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = {}
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    print(fib(n))