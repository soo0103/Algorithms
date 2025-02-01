import sys

N = int(sys.stdin.readline())

word = list(sys.stdin.readline().strip())

for i in range(N - 1):
    other = sys.stdin.readline().strip()

    for j in range(len(word)):
        if word[j] == other[j]:
            continue
        else:
            word[j] = "?"

print("".join(word))