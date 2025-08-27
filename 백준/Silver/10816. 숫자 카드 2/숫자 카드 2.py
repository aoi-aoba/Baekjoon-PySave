import sys
input = sys.stdin.readline

n = int(input())
numDict = {}
for i in input().split():
    if i not in numDict:
        numDict[i] = 1
    else:
        numDict[i] = numDict.get(i) + 1

m = int(input())
ans = [numDict.get(i) if i in numDict else 0 for i in input().split()]
print(*ans)