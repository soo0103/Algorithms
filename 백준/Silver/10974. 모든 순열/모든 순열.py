import sys

def seq():
    prev = 0
    
    if len(s) == N:
        print(' '.join(map(str, s)))
        return

    for i in range(N):
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            s.append(arr[i])
            prev = arr[i]
            seq()
            s.pop()
            visited[i] = False

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    arr = [i for i in range(1, N + 1)]
    visited = [False] * N
    s = []

    seq()