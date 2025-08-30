import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def to_list(self):
        return self.items

stack = Stack()
K = int(input())
for _ in range(K):
    temp = int(input())
    if temp == 0:
        stack.pop()
    else:
        stack.push(temp)

print(sum(stack.to_list()))