def makeStar(i, j, n):
    if n == 1:
        ans[i][j] = True
        return
    k = n // 3
    for r in range(3):
        for c in range(3):
            if r != 1 or c != 1:
                makeStar(i + r * k, j + c * k, k)

N = int(input())
ans = [[False] * N for _ in range(N)]
makeStar(0, 0, N)

print("\n".join("".join("*" if ans[i][j] else " " for j in range(N)) for i in range(N)))