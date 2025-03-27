import sys

INF = int(1e9)

def get_force(start, end):
    if start == 0:
        return 2
    elif start == end:
        return 1
    elif abs(start - end) == 2:
        return 4
    else:
        return 3

if __name__ == "__main__":
    cmd = list(map(int, sys.stdin.readline().split()))

    dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(cmd))]
    dp[0][0][0] = 0
    result = INF

    for i in range(len(cmd) - 1):
        for l in range(5):
            for r in range(5):
                dp[i + 1][cmd[i]][r] = min(dp[i + 1][cmd[i]][r], dp[i][l][r] + get_force(l, cmd[i]))
                dp[i + 1][l][cmd[i]] = min(dp[i + 1][l][cmd[i]], dp[i][l][r] + get_force(r, cmd[i]))

print(min(map(min, dp[len(cmd) - 1])))