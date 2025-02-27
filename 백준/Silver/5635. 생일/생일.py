import sys

n = int(sys.stdin.readline())
students = [list(sys.stdin.readline().split()) for _ in range(n)]

for i in range(len(students)):
    students[i][1:] = map(int, students[i][1:])

students.sort(key = lambda x: (-x[3], -x[2], -x[1]))

print(students[0][0])
print(students[-1][0])