import sys
input = sys.stdin.readline

n = int(input())
wordLst = dict()

for _ in range(n):
    word = input().rstrip()
    if len(word) == 1:
        wordLst[word] = word
    elif len(word) == 2:
        wordLst[(word[0], word[-1])] = word
    else:
        wordLst[(word[0], word[-1], ''.join(sorted(word[1:-1])))] = word

m = int(input())
ans = []

for word in input().strip().split():
    if len(word) == 1:
        ans.append(wordLst[word])
    elif len(word) == 2:
        ans.append(wordLst[(word[0], word[-1])])
    else:
        ans.append(wordLst[(word[0], word[-1], ''.join(sorted(word[1:-1])))])

print(' '.join(ans))
