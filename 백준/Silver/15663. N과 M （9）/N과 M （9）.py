import sys

def seq():
    prev = 0
    
    if len(s) == M:
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
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    s = []
    visited = [False for _ in range(N)]
    
    seq()