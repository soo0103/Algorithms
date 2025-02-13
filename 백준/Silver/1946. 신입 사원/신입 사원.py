import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    applicants = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    applicants.sort()

    grade = applicants[0][1]
    cnt = 1

    for i in range(1, N):
        if applicants[i][1] < grade:
            grade = applicants[i][1]
            cnt += 1

    print(cnt)