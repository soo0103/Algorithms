import sys

ah = sys.stdin.readline().strip()
doctor = sys.stdin.readline().strip()

if len(ah) >= len(doctor):
    print("go")
else:
    print("no")