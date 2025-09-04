def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            rows[x] = i
            # 정말 놓을 수 있는지 체크
            if can_drop(x):
                n_queens(x + 1)

def can_drop(x):
    for i in range(x):
        if rows[i] == rows[x] or abs(rows[x] - rows[i]) == abs(x - i):
            return False
    # 이전 칸에 놓인 퀸들과 같은 행에 놓거나 대각선 놓이지 않을 때
    return True

n = int(input())
rows = [0] * n
ans = 0

n_queens(0)
print(ans)