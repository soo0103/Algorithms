import sys

def dfs(row, col, cnt):
    global count
    r, c, cnt = row, col, cnt
    count = max(count, cnt)

    visited[ord(board[r][c]) - 65] = True
    n = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

    for point in n:
        if 0 <= point[0] < R and 0 <= point[1] < C:
            if not visited[ord(board[point[0]][point[1]]) - 65]:
                dfs(point[0], point[1], cnt + 1)
                visited[ord(board[point[0]][point[1]]) - 65] = False

if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(R)]
    count = 0
    visited = [False for _ in range(26)]

    dfs(0, 0, 1)

    print(count)