board = [[False] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    p, q = map(int, input().split())
    for i in range(p, p + 10):
        for j in range(q, q + 10):
            board[i][j] = True

res = 0
for line in board:
    res += line.count(True)

print(res)