import math

for i in range(int(input())):
    N, M = map(int, input().split())
    print(math.comb(M, N))