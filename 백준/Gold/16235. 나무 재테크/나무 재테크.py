import sys
from collections import deque, defaultdict

N, M, K = map(int, sys.stdin.readline().split())

cnt = 0
earth = [[5] * N for _ in range(N)]
nutrient = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
age = [[deque() for _ in range(N)] for _ in range(N)]
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    age[x - 1][y - 1].append(z)

for _ in range(K):
    new_trees = defaultdict(int)

    for r in range(N):
        for c in range(N):
            if not age[r][c]:
                continue
            
            live = deque()
            dead_nutrient = 0
            
            while age[r][c]:
                tree = age[r][c].popleft()
                if earth[r][c] >= tree:
                    earth[r][c] -= tree
                    live.append(tree + 1)

                    if (tree + 1) % 5 == 0:
                        new_trees[(r, c)] += 1
                else:
                    dead_nutrient += tree // 2
            
            age[r][c] = live
            earth[r][c] += dead_nutrient

    for (r, c), count in new_trees.items():
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                age[nr][nc].extendleft([1] * count)

    for r in range(N):
        for c in range(N):
            earth[r][c] += nutrient[r][c]

cnt = sum(len(age[r][c]) for r in range(N) for c in range(N))
print(cnt)