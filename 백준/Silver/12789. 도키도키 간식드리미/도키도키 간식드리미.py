class Stack:
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1] if not self.is_empty() else -1
	def is_empty(self):
		return not self.items

import sys
input = sys.stdin.readline

stack1 = Stack()
stack2 = Stack()

n = int(input())
for i in input().split()[::-1]:
	stack1.push(int(i))

now = 1
while True:
	if stack1.peek() == now:
		now += 1
		stack1.pop()
	elif stack2.peek() == now:
		now += 1
		stack2.pop()
	elif not stack1.is_empty() and stack1.peek() != now:
		stack2.push(stack1.pop())
	elif stack1.is_empty() and stack2.peek != now:
		break

print("Nice" if stack1.is_empty() and stack2.is_empty() else "Sad")