import sys
from collections import deque

input = sys.stdin.readline
d = deque()
n = int(input())
printArr = []

for _ in range(n):
	op = input().split()
	if op[0] == '1':
		d.appendleft(op[1])
	elif op[0] == '2':
		d.append(op[1])
	elif op[0] == '3':
		printArr.append(d.popleft() if d else "-1")
	elif op[0] == '4':
		printArr.append(d.pop() if d else "-1")
	elif op[0] == '5':
		printArr.append(str(len(d)))
	elif op[0] == '6':
		printArr.append("1" if not d else "0")
	elif op[0] == '7':
		printArr.append(d[0] if d else "-1")
	else:
		printArr.append(d[-1] if d else "-1")

print("\n".join(printArr))