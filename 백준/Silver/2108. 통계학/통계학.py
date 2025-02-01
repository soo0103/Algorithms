import sys
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

dic = dict()

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic = []

for j in dic:
    if mx == dic[j]:
        mx_dic.append(j)

print(round(sum(arr) / len(arr)))
print(arr[len(arr) // 2])

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
    
print(max(arr) - min(arr))