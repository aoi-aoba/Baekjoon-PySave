import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wordSet = set(input().strip() for _ in range(n))

print(sum(1 for _ in range(m) if input().strip() in wordSet))