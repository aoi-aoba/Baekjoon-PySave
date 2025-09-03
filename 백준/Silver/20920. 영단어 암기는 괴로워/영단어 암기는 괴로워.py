import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wordDict = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

print("\n".join(sorted(set(wordDict), key=lambda w : (-wordDict[w], -len(w), w))))