import math

for i in range(int(input())):
    n, m = map(int, input().split())
    print(math.comb(n, m) if n > m else math.comb(m, n))