n = int(input())
scores = list(map(int, input().split()))
maxVal = max(scores)
result = 0
for score in scores:
    score = score / maxVal * 100
    result += score
print(result / n)