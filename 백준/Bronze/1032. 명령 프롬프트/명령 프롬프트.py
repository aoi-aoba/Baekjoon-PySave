import sys
input = sys.stdin.readline

n = int(input())
s = [ch for ch in input().rstrip()]

for _ in range(n - 1):
    t = input().rstrip()
    for i in range(len(s)):
        if s[i] != t[i]:
            s[i] = '?'

print(''.join(ch for ch in s))