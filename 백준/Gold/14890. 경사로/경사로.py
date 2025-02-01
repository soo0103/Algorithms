import sys

N, L = map(int, sys.stdin.readline().split())

guidance = []

for _ in range(N):
    guidance.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * N for _ in range(N)]

def isLineIsPassable(idx, isHorizontal):
    line = []
    if isHorizontal:
        for i in range(N):
            line.append(guidance[idx][i])
    else:
        for i in range(N):
            line.append(guidance[i][idx])

    visited = [False for _ in range(N)]
    now = 0

    while 1:
        if now == N - 1:
            return True
        if line[now] == line[now + 1]:
            now += 1
            continue
        elif abs(line[now] - line[now + 1]) > 1:
            return False
        else:
            if line[now] - line[now + 1] == 1:
                flag = True

                for i in range(1, L + 1):
                    if 0 <= now + i < N:
                        if not visited[now + i]:
                            if line[now + 1] != line[now + i]:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                    
                if flag:
                    for i in range(1, L + 1):
                        visited[now + i] = True
                    now += L
                else:
                    return False

            elif line[now] - line[now + 1] == -1:
                flag = True

                for i in range(0, L):
                    if 0 <= now - i < N:
                        if not visited[now - i]:
                            if line[now] != line[now - i]:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                
                if flag:
                    for i in range(0, L):
                        visited[now - i] = True
                    now += 1
                else:
                    return False

cnt = 0

for i in range(N):
    cnt += int(isLineIsPassable(i, True))
    cnt += int(isLineIsPassable(i, False))

print(cnt)