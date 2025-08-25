n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((y, x))

points.sort()

for x, y in points:
    print(y, x)