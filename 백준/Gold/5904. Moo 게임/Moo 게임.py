import sys

def cnt(k):
    if k == 0:
        return 3
    else:
        return 2 * cnt(k - 1) + k + 3

def Moo(N, k):
    if N <= 3:
        arr = ['m', 'o', 'o']
        return arr[N - 1]
    elif N <= cnt(k):
        if N <= cnt(k - 1):
            return Moo(N, k - 1)
        elif N > cnt(k - 1) + k + 3:
            N -= (cnt(k - 1) + k + 3)
            return Moo(N, k - 1)
        else:
            N -= cnt(k - 1)
            if N == 1:
                return 'm'
            else:
                return 'o'
    else:
        return Moo(N, k + 1)

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    print(Moo(N, 1))