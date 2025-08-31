import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
form = input().split()
values = input().split()
qs = deque([int(values[i]) for i in range(n) if form[i] == '0'])

m = int(input())
inputs = list(map(int, input().split()))
res = []

for item in inputs:
	qs.appendleft(item)
	res.append(qs.pop())

print(*res)
