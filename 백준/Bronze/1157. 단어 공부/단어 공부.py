import sys

word = sys.stdin.readline().upper().strip()

unique = list(set(word))

arr = []

for i in unique:
    cnt = word.count(i)
    arr.append(cnt)

if arr.count(max(arr)) > 1:
    print("?")
else:
    print(unique[arr.index(max(arr))])