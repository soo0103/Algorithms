import sys

def dfs(idx, cnt):
    global chickenDistance

    if cnt == M:
        minDistance = 0

        for h in home:
            distance = INF

            for v in range(len(visited)):
                if visited[v]:
                    d = abs(h[0] - chicken[v][0]) + abs(h[1] - chicken[v][1])
                    distance = min(distance, d)

            minDistance += distance 
        
        chickenDistance = min(chickenDistance, minDistance)

        return

    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False
            
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    home = []
    chicken = []
    INF = int(1e9)
    chickenDistance = INF

    for r in range(N):
        city = list(map(int, sys.stdin.readline().split()))

        for c in range(N):
            if city[c] == 1:
                home.append((r, c))
            elif city[c] == 2:
                chicken.append((r, c))

    visited = [False] * len(chicken)

    dfs(0,0)

    print(chickenDistance)