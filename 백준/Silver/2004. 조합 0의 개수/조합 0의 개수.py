import sys

def count(n, k):
    result = 0
    temp = k
    
    while temp <= n:
        result += n // temp
        temp *= k
    
    return result

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    t = count(n, 2) - count(m, 2) - count(n - m, 2)
    f = count(n, 5) - count(m, 5) - count(n - m, 5)

    print(min(t, f))