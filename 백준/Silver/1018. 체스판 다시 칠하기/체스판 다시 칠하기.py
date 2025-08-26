n, m = map(int, input().split())
board = []
res = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        drawStartB = drawStartW = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # 특정 칸의 인덱스 합이 짝수
                if (a + b) % 2 == 0:
                    # BWBW..로 시작하면 인덱스 합 짝수 위치가 B여야 함
                    if board[a][b] != 'B':
                        drawStartB += 1
                    # 반대로 WBWB로 시작하면 인덱스 합 짝수 위치는 W
                    if board[a][b] != 'W':
                        drawStartW += 1
                else:
                    if board[a][b] != 'W':
                        drawStartB += 1
                    if board[a][b] != 'B':
                        drawStartW += 1
        res.append(drawStartB)
        res.append(drawStartW)
print(min(res))