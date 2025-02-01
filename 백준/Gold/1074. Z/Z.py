import sys

def zQuest(N, r, c):
    if N == 1:
        return(2 * r + c)
    else:
        if r < 2 ** (N - 1) and c < 2 ** (N - 1):
            return zQuest(N - 1, r, c)
        elif r < 2 ** (N - 1) and c >= 2 ** (N - 1):
            return zQuest(N - 1, r, c - 2 ** (N - 1)) + 2 ** (2 * N - 2)
        elif r >= 2 ** (N - 1) and c < 2 ** (N - 1):
            return zQuest(N - 1, r - 2 ** (N - 1), c) + 2 ** (2 * N - 1)
        else:
            return zQuest(N - 1, r - 2 ** (N - 1), c - 2 ** (N - 1)) + 3 * 2 ** (2 * N - 2)
    

if __name__ == "__main__":
    N, r, c = map(int, sys.stdin.readline().split())
    
    print(zQuest(N, r, c))