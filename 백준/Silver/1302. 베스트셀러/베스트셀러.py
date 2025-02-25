import sys

books = {}

N = int(sys.stdin.readline())

for _ in range(N):
    title = sys.stdin.readline().strip()

    if title in books:
        books[title] += 1
    else:
        books[title] = 1

books = sorted(books.items(), key = lambda x: (-x[1], x[0]))

print(books[0][0])