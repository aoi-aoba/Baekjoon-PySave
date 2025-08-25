n = int(input())
strDict = set(input() for _ in range(n))
strDict = sorted(strDict, key=lambda s: (len(s), s))
for word in strDict:
    print(word)