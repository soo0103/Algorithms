import sys

N = int(sys.stdin.readline())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = [0, 1, 2, 3, 4, 5, 6]
day = 13
cnt = 0

for i in range(2019, N + 1):
    if i % 400 == 0:
        month[1] = 29
    elif i % 100 != 0 and i % 4 == 0:
        month[1] = 29
    else:
        month[1] = 28
    for j in month:
        if week[day % 7] == 4:
            cnt += 1
        day += j
        
print(cnt)