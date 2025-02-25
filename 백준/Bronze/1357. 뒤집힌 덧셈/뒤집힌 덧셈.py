import sys

def Rev(num):
    return int(''.join(list(reversed(list(num)))))

if __name__ == "__main__":
    X, Y = sys.stdin.readline().split()

    print(Rev(str(Rev(X) + Rev(Y))))