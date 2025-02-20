import sys

lectures = ["swimming", "bowling", "soccer"]

lecture_map = {lectures[i]: i for i in range(len(lectures))}

n = int(sys.stdin.readline().strip())

first_choice = ["swimming"] * n
print(" ".join(first_choice))
sys.stdout.flush()

fail_lectures = sys.stdin.readline().strip().split()

final_choices = []

for fail_lecture in fail_lectures:
    idx = 2 if lecture_map[fail_lecture] == 1 else 1
    final_choices.append(lectures[idx])

print(" ".join(final_choices))
sys.stdout.flush()