import sys

X, Y = map(int, sys.stdin.readline().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(X - 1):
    Y += days[i]

print(weekday[Y % 7])