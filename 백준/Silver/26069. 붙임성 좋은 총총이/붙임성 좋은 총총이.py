import sys
input = sys.stdin.readline

n = int(input())
dancers = {"ChongChong"}

for _ in range(n):
    a, b = input().rstrip().split()

    if a in dancers:
        dancers.add(b)

    if b in dancers:
        dancers.add(a)

print(len(dancers))