import sys

N = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

drawing_paper = [[0] * 101 for _ in range(101)]
result = 0

for x, y in papers:
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            drawing_paper[i][j] = 1

for i in drawing_paper:
    result += sum(i)

print(result)