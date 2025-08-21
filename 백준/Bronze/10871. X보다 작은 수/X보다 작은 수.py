import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
numList = []

for i in sys.stdin.readline().rstrip().split():
    if int(i) < x: numList.append(int(i))

print(*numList)