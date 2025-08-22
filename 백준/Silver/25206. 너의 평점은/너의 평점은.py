import sys
sumScore = sumGrade = 0

for line in sys.stdin.readlines():
    name, score, grade = map(str, line.split())

    if grade == "P": continue
    elif ord("E") - ord(grade[0]) >= 1: gradeScore = ord("E") - ord(grade[0])
    else: gradeScore = 0

    if grade.endswith("+"): gradeScore += 0.5
    elif grade.endswith("-"): gradeScore -= 0.5

    sumScore += float(score)
    sumGrade += float(score) * gradeScore

print(sumGrade / sumScore)