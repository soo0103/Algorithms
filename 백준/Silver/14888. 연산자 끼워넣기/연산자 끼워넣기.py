import sys

def calc(cnt, num, s, m, x, d):
    global maxvalue
    global minvalue

    if cnt == N:
        maxvalue = max(maxvalue, num)
        minvalue = min(minvalue, num)
        return

    if s:
        calc(cnt + 1, num + eq[cnt], s - 1, m, x, d)
    if m:
        calc(cnt + 1, num  - eq[cnt], s, m - 1, x, d)
    if x:
        calc(cnt + 1, num * eq[cnt], s, m, x - 1, d)
    if d:
        calc(cnt + 1, int(num / eq[cnt]), s, m, x, d - 1)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    eq = list(map(int, sys.stdin.readline().split()))
    op = list(map(int, sys.stdin.readline().split()))
    cnt = 1
    maxvalue = -1e9
    minvalue = 1e9

    calc(cnt, eq[0], op[0], op[1], op[2], op[3])
    
    print(int(maxvalue))
    print(int(minvalue))