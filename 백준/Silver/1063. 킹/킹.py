import sys

move = {
    'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1],
    'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]
}

King, Rock, N = sys.stdin.readline().split()
k = [ord(King[0]) - 64, int(King[1])]
r = [ord(Rock[0]) - 64, int(Rock[1])]

for _ in range(int(N)):
    cmd = sys.stdin.readline().strip()

    if cmd in move:
        nx, ny = k[0] + move[cmd][0], k[1] + move[cmd][1]

        if 1 <= nx <= 8 and 1 <= ny <= 8:
            if [nx, ny] == r:
                rx, ry = r[0] + move[cmd][0], r[1] + move[cmd][1]
                
                if 1 <= rx <= 8 and 1 <= ry <= 8:
                    k = [nx, ny]
                    r = [rx, ry]
            else:
                k = [nx, ny]

print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(r[0] + 64)}{r[1]}')