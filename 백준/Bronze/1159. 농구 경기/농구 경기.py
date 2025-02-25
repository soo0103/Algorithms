import sys

names = {}

N = int(sys.stdin.readline())

for _ in range(N):
    name = sys.stdin.readline().strip()

    if name[0] in names:
        names[name[0]] += 1
    else:
        names[name[0]] = 1

names = sorted(names.items(), key = lambda x: x[0])

result = ''

for key, value in names:
    if value >= 5:
        result += key

if not result:
    print("PREDAJA")
else:
    print(result)