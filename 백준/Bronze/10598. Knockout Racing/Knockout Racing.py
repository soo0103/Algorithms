import sys

def get_position(ai, bi, time):
    T = 2 * abs(ai - bi)
    mod_t = time % T
    
    if mod_t <= abs(ai - bi):
        return ai + (1 if ai < bi else -1) * mod_t
    else:
        return bi + (1 if bi < ai else -1) * (mod_t - abs(ai - bi))

n, m = map(int, sys.stdin.readline().split())
cars = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

results = []

for xj, yj, tj in queries:
    count = 0
    for ai, bi in cars:
        pos = get_position(ai, bi, tj)

        if xj <= pos <= yj:
            count += 1

    results.append(str(count))

print(*results, sep='\n')