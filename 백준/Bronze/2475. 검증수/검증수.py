res = 0
for i in input().split():
    res += int(i) * int(i)
print(res % 10)