import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    people = [x for x in range(1, n + 1)]

    for floor in range(k):
        for room in range(1, n):
            people[room] += people[room - 1]
    
    print(people[n - 1])