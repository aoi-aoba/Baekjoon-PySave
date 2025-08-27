import sys
input = sys.stdin.readline

n = int(input())
dataset = set()

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        dataset.add(name)
    else:
        dataset.discard(name)

for name in sorted(dataset, reverse=True):
    print(name)