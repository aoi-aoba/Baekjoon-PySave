import sys
sumScore = sumGrade = 0

for line in sys.stdin.readlines():
    name, score, grade = map(str, line.split())
    if (grade == "P"): continue

    if (grade.startswith("A")): gradeScore = 4.0
    elif (grade.startswith("B")): gradeScore = 3.0
    elif (grade.startswith("C")): gradeScore = 2.0
    elif (grade.startswith("D")): gradeScore = 1.0
    else: gradeScore = 0

    if (grade.endswith("+")): gradeScore += 0.5
    elif (grade.endswith("-")): gradeScore -= 0.5

    sumScore += float(score)
    sumGrade += float(score) * gradeScore

print(sumGrade / sumScore)