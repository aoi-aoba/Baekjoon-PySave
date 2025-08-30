import sys
input = sys.stdin.readline

ans = []

while True:
    stack = []
    line = input().rstrip()
    if line == ".":
        break

    for ch in line:
        if ch in {'(', ')', '[', ']'}:
            if not stack:
                stack.append(ch)
            elif stack[-1] == '(' and ch == ')':
                stack.pop()
            elif stack[-1] == '[' and ch == ']':
                stack.pop()
            else:
                stack.append(ch)

    ans.append("yes" if not stack else "no")

print("\n".join(ans))