import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokeDict = {}

for i in range(1, n + 1):
    name = input().strip()
    pokeDict[i] = name
    pokeDict[name] = i

ans = []
for _ in range(m):
    q = input().strip()
    if q.isdigit():
        ans.append(pokeDict[int(q)])
    else:
        ans.append(str(pokeDict[q]))
        
print("\n".join(ans))