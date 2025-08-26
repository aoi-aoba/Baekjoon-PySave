n = int(input())
low = n - 9 * len(str(n))
if low < 0 : low = 0

for i in range(low, n):
    sumCase = i + sum(map(int, str(i)))
    if sumCase == n:
        print(i)
        break
    if i == n - 1:
        print(0)