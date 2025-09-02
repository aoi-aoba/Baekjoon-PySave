def fact(n):
    if n <= 1:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def comb(n, r):
    if n < r:
        temp = n; n = r; r = temp
    return fact(n) // (fact(n - r) * fact(r))


for i in range(int(input())):
    N, M = map(int, input().split())
    print(comb(N, M))