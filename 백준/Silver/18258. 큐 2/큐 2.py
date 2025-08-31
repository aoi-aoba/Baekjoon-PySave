import sys
from collections import deque

input = sys.stdin.readline

q = deque()
n = int(input())
printArr = []

for _ in range(n):
	op = input().rstrip()
	if op == "pop":
		printArr.append(q.popleft() if q else "-1")
	elif op == "size":
		printArr.append(str(len(q)))
	elif op == "empty":
		printArr.append("1" if not q else "0")
	elif op == "front":
		printArr.append(q[0] if q else "-1")
	elif op == "back":
		printArr.append(q[-1] if q else "-1")
	else:
		q.append(op.split()[1])

print("\n".join(printArr))