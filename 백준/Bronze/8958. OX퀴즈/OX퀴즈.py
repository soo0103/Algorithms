import sys

T = int(sys.stdin.readline())

for _ in range(T):
    quiz = sys.stdin.readline().strip()
    score = 0
    value = 0

    for i in quiz:
        if i == 'O':
            value += 1
            score += value
        else:
            value = 0

    print(score)