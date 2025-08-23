T = int(input())
xpos = []
ypos = []
for _ in range(T):
    x, y = map(int, input().split())
    xpos.append(x)
    ypos.append(y)
print((max(xpos)-min(xpos))*(max(ypos)-min(ypos)))