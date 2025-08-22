t = int(input())
for i in range(t):
    s = input()
    streak = score = 0
    for j in s:
        if j == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)