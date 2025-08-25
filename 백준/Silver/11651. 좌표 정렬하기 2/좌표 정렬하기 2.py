import sys

n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))
points.sort(key=lambda point: (point[1], point[0]))
for x, y in points:
    print(x, y)