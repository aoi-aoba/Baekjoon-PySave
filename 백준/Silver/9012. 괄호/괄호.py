import sys
input = sys.stdin.readline

ans = []
T = int(input())

for _ in range(T):
    stack = []
    line = input().strip()

    for ch in line:
        if len(stack) == 0:
            stack.append(ch)
        elif stack[-1] == '(' and ch == ')' :
            stack.pop()
        else:
            stack.append(ch)

    ans.append("YES" if len(stack) == 0 else "NO")

print("\n".join(ans))