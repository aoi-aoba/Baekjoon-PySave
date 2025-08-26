n = int(input())
res = 0
for i in range(1, n+1):
    sumCase = i + sum(int(j) for j in str(i))
    if sumCase == n:
        res = i
        break
print(res)