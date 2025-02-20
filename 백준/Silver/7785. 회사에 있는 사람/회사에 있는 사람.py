import sys

n = int(sys.stdin.readline())

company = {}

for _ in range(n):
    name, log = sys.stdin.readline().split()

    if log == "leave":
        company.pop(name)
    else:
        company[name] = 1

company = sorted(company.items(), reverse = True)

for name, log in company:
    print(name)