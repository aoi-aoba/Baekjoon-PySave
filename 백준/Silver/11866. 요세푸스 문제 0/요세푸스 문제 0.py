import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n, k = map(int, input().split())
printArr = []

for i in range(1, n + 1):
	q.append(i)
while q:
	for i in range(k - 1):
		q.append(q.popleft())
	printArr.append(str(q.popleft()))

print("<" + ", ".join(printArr) + ">")