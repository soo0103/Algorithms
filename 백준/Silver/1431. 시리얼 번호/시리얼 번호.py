import sys

guitars = {}

N = int(sys.stdin.readline())


for _ in range(N):
    serial = sys.stdin.readline().strip()

    num = 0

    for i in range(len(serial)):
        if serial[i].isnumeric():
            num += int(serial[i])
    
    guitars[serial] = num

guitars = sorted(guitars.items(), key = lambda x: (len(x[0]), x[1], x[0]))

for i in range(N):
    print(guitars[i][0])