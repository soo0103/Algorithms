import sys

t = int(sys.stdin.readline())

for _ in range(t):
	arr = sys.stdin.readline().rstrip()
	password = []
	cursor = []

	for i in arr:
		if i == '<':
			if password:
				cursor.append(password.pop()) 
		elif i == '>':
			if cursor:
				password.append(cursor.pop())
		elif i == '-':
			if password:
				password.pop()
		else:
			password.append(i)
            
	print("".join(password),"".join(cursor[::-1]),sep="")