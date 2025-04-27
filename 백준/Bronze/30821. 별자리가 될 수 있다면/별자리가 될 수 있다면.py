import sys

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    print(fact(N) // (fact(N - 5) * fact(5)))