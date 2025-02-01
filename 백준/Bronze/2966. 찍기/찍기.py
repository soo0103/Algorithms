import sys

sg = ["A", "B", "C"] * 34
cy = ["B", "A", "B", "C"] * 25
hj = ["C", "C", "A", "A", "B", "B"] * 17

sg_score = 0
cy_score = 0
hj_score = 0

N = int(sys.stdin.readline())
test = list(sys.stdin.readline().strip())

for i in range(N):
    if test[i] == sg[i]:
        sg_score += 1
    if test[i] == cy[i]:
        cy_score += 1
    if test[i] == hj[i]:
        hj_score += 1

print(max(sg_score, cy_score, hj_score))

if max(sg_score, cy_score, hj_score) == sg_score:
    print("Adrian")
if max(sg_score, cy_score, hj_score) == cy_score:
    print("Bruno")
if max(sg_score, cy_score, hj_score) == hj_score:
    print("Goran")