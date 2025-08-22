a, b = map(int, input().split())
if a == 0 and b < 45 : a += 24
print(a - 1 if b < 45 else a, b - 45 + 60 if b < 45 else b - 45)