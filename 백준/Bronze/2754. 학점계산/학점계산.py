grade = input()

if grade.startswith("A"): score = 4.0
elif grade.startswith("B"): score = 3.0
elif grade.startswith("C"): score = 2.0
elif grade.startswith("D"): score = 1.0
else: score = 0.0

if grade.endswith("+"): score += 0.3
elif grade.endswith("-"): score -= 0.3

print(score)