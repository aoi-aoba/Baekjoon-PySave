import sys
from collections import deque

def pop_balloon(dq):
	num, move = dq.popleft()
	result.append(str(num))
	return move

input = sys.stdin.readline
n = int(input())
moves = list(map(int, input().split()))
deq = deque((i + 1, moves[i]) for i in range(n))

result = []
move = pop_balloon(deq)

while deq:
	if move > 0:
		deq.rotate(-(move - 1))
	else:
		deq.rotate(-move)
	# rotate(n) : n > 0 일 때 오른쪽 / n < 0 일 때 왼쪽 회전
	move = pop_balloon(deq)

print(' '.join(result))