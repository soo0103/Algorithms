import sys

K = int(sys.stdin.readline())

for i in range(1, K + 1):
    scores = list(map(int, sys.stdin.readline().split()))[1:]
    scores.sort(reverse=True)

    largest_gap = 0

    for j in range(len(scores) - 1):
        if scores[j] - scores[j + 1] > largest_gap:
            largest_gap = scores[j] - scores[j + 1]
    
    print(f"Class {i}\nMax {max(scores)}, Min {min(scores)}, Largest gap {largest_gap}")
