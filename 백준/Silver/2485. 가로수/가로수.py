import sys

def get_gcd(x, y):
    if x % y == 0:
        return y
    elif y == 0:
        return x
    else:
        return get_gcd(y, x % y)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    trees = [int(sys.stdin.readline()) for _ in range(N)]

    sub = [trees[i + 1] - trees[i] for i in range(N - 1)]
    gcd = sub[0]
    cnt = 0

    for s in sub:
        gcd = get_gcd(gcd, s)

    for s in sub:
        cnt += s // gcd - 1

    print(cnt)