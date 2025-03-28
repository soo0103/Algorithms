import sys

word = sys.stdin.readline().strip()

dial = "3334445556667778888999"
time = 0

for w in word:
    if w not in "WXYZ":
        time += int(dial[ord(w) - 65])
    else:
        time += 10

print(time)