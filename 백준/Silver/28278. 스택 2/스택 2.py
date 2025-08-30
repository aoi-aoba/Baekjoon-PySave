import sys
input = sys.stdin.readline

def is_empty(data):
    return True if len(data) == 0 else False

t = int(input())
stack = []
printRes = []
for _ in range(t):
    op = input()
    if op[0] == '1':
        stack.append(op.split()[1])
    elif op[0] == '2':
        printRes.append(stack.pop() if not is_empty(stack) else "-1")
    elif op[0] == '3':
        printRes.append(str(len(stack)))
    elif op[0] == '4':
        printRes.append("1" if is_empty(stack) else "0")
    else:
        printRes.append(stack[-1] if not is_empty(stack) else "-1")

print("\n".join(printRes))