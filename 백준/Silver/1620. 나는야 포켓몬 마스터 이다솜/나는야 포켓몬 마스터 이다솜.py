import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokeDict = dict()

for i in range(1, n + 1):
    name = input().strip()
    pokeDict[str(i)] = name
    pokeDict[name] = i

for _ in range(1, m + 1):
    print(pokeDict.get(input().strip()))