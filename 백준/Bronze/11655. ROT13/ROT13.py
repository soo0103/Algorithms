import sys

S = sys.stdin.readline().rstrip()

answer = ''

for i in S:
    if 'a'<= i <= 'z':
        i = ord(i) + 13
        
        if i > 122:
            i -= 26
        
        answer += chr(i)
    elif 'A' <= i <='Z':
        i = ord(i) + 13
        
        if i > 90:
            i -= 26
        
        answer += chr(i)
    else:
        answer += i

print(answer)