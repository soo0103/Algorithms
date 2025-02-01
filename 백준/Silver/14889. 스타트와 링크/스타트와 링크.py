import sys

def startlink(L, idx):
    global result
    
    if L == N//2:
        A = 0
        B = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += arr[i][j]
                elif not visited[i] and not visited[j]:
                    B += arr[i][j]
        result = min(result, abs(A - B))

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            startlink(L + 1, i + 1)
            visited[i] = False

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []

    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    result = 2147000000
    visited = [False for _ in range(N)]
    
    startlink(0, 0)
    
    print(result)