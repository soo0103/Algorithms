import sys

def explore():
    time = 0
    longest = 0

    for i in range(4):
        r, c, d = PR, PC, i
        cnt = 0

        while 1:
            cnt += 1
            r = r + dr[d]
            c = c + dc[d]
            if signal[r][c] == 'C':
                break
            if signal[r][c] == '/':
                d = change1[d]
            if signal[r][c] == '\\':
                d = change2[d]
            if r == PR and c == PC and d == i:
                print(dir[i])
                print("Voyager")
                return

        if cnt > time:
            time = cnt
            longest = i

    print(dir[longest])
    print(time)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    signal = [['C'] * (M + 2)]

    for _ in range(N):
        signal.append(['C'] + list(sys.stdin.readline().strip()) + ['C'])

    signal.append(['C'] * (M + 2))
    
    PR, PC = map(int, sys.stdin.readline().split())
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']
    change1 = [1, 0, 3, 2]
    change2 = [3, 2, 1, 0]

    explore()