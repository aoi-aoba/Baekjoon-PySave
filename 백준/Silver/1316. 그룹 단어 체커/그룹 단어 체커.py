n = int(input())
ans = 0
for i in range(n):
    word = input()
    alpha = [-1 for _ in range(26)]
    isGroupWord = True
    for i in range(len(word)):
        alphaNum = ord(word[i]) - ord('a')
        if alpha[alphaNum] == -1 or alpha[alphaNum] == i - 1:
            alpha[alphaNum] = i
        else:
            isGroupWord = False
    if isGroupWord : ans += 1
print(ans)