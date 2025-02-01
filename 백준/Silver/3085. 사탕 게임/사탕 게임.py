import sys

def count():
    for l in range(N):
        global value
        cnt = 1 

        for m in range(N - 1):
            if candy[l][m] == candy[l][m + 1]:
                cnt += 1
            else:
                cnt = 1
            value = max(value, cnt)

        cnt = 1

        for m in range(N - 1):
            if candy[m][l] == candy[m + 1][l]:
                cnt += 1
            else:
                cnt = 1
            value = max(value, cnt)
            
    return value

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    candy = []
    value = 1
    num = 1
    
    for _ in range(N):
        candy.append(list(sys.stdin.readline().rstrip()))

    for i in range(N):
        for j in range(N):
            if j + 1 < N and candy[i][j] != candy[i][j + 1]:
                candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
                count()
                num = max(value, num)
                candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

            if i + 1 < N and candy[i][j] != candy[i + 1][j]:
                candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
                count()
                num = max(value, num)
                candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

    print(num)