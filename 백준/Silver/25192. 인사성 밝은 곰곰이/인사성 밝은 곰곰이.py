import sys
input = sys.stdin.readline

n = int(input())
ans = 0
nameSet = set()
for _ in range(n):
    line = input().rstrip()
    if line == "ENTER":
        ans += len(nameSet)
        nameSet = set()
    else:
        nameSet.add(line)
print(ans + len(nameSet))