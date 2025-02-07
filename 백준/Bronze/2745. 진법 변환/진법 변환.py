import sys

N, B = sys.stdin.readline().split()

form = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0

for i, num in enumerate(N[::-1]):
    ans += (int(B) ** i) * form.index(num)

print(ans)