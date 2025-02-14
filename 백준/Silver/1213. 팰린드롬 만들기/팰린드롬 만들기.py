import sys

arr = list(sys.stdin.readline().strip())
arr.sort()

word = {}
cnt = 0
mid = ''
result = ''

for i in arr:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

for key, value in word.items():
    if value % 2 != 0:
        cnt += 1
        mid = key

    if cnt >= 2:
        print("I'm Sorry Hansoo")
        break
        
    result += key * (value // 2)

result = result + mid + result[::-1]

if len(arr) == len(result):
    print(result)