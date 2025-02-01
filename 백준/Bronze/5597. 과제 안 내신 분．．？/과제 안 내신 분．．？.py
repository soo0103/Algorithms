import sys

students = [i for i in range(1, 31)]

for _ in range(28):
    n = int(sys.stdin.readline())
    students.remove(n)

print(min(students))
print(max(students))