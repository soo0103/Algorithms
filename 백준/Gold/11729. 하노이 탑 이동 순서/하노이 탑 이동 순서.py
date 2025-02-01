import sys

def hanoi(n, frm, tmp, to):
    if n == 1:
        print(frm, to)
    else:
        hanoi(n - 1, frm, to, tmp)
        print(frm, to)
        hanoi(n - 1, tmp, frm, to)

if __name__ == "__main__":
    K = int(sys.stdin.readline())

    print(2 ** K - 1)
    hanoi(K, 1, 2, 3) 