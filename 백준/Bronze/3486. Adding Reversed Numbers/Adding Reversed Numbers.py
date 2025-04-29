import sys

def change_num(x):
    while x[-1] == '0':
        x = x[:-1]
    return int(x[::-1])

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    for _ in range(N):
        a, b = map(str, sys.stdin.readline().split())

        result = change_num(a) + change_num(b)

        print(int(str(result)[::-1]))