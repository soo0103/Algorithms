import sys

N = int(sys.stdin.readline())
text = sys.stdin.readline().strip()
b = text.count("bigdata")
s = text.count("security")

if b > s:
    print("bigdata?")
elif b < s:
    print("security!")
else:
    print("bigdata? security!")