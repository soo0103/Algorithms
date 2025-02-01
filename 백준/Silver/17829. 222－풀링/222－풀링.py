import sys

def CNN(x, y, N):
    if N == 2:
        new = [arr[x][y], arr[x][y + 1], arr[x + 1][y], arr[x + 1][y + 1]]
        new.sort()
        return new[-2]
    else:
        new = [CNN(x, y, N // 2), CNN(x, y + N // 2, N // 2), CNN(x + N // 2, y, N // 2), CNN(x + N // 2, y + N // 2, N // 2)]
        new.sort()
        return new[-2]
    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []

    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    print(CNN(0, 0, N))