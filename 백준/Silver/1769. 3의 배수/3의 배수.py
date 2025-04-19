import sys

X = sys.stdin.readline().strip()

cnt = 0
result = int(X)

while len(X) > 1:
    result = 0

    for i in X:
        result += int(i)

    X = str(result)
    cnt += 1

print(cnt)

if int(result) % 3 == 0:
    print("YES")
else:
    print("NO")