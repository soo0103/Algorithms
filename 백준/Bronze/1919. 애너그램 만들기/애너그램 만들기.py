import sys

w1 = sys.stdin.readline().strip()
w2 = sys.stdin.readline().strip()

cnt = 0

for i in range(len(w1)):
    c = w1[i]

    if c != ' ':
        cnt1 = w1.count(c)
        cnt2 = w2.count(c)

        cnt += abs(cnt1 - cnt2)

        w1 = w1.replace(c, ' ')
        w2 = w2.replace(c, ' ')

for i in range(len(w2)):
    c = w2[i]

    if w2[i] != ' ':
        cnt1 = w1.count(c)
        cnt2 = w2.count(c)

        cnt += abs(cnt1 - cnt2)

        w1 = w1.replace(c, ' ')
        w2 = w2.replace(c, ' ')

print(cnt)