import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wordSet = set(input().strip() for _ in range(n))

result = 0
for _ in range(m):
    if input().strip() in wordSet:
        result += 1

print(result)