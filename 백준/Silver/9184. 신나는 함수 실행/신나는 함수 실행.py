dp_array = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def dp():
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if i < j < k:
                    dp_array[i][j][k] = dp_array[i][j][k-1] + dp_array[i][j-1][k-1] - dp_array[i][j-1][k]
                else:
                    dp_array[i][j][k] = dp_array[i-1][j][k] + dp_array[i-1][j-1][k] + dp_array[i-1][j][k-1] - dp_array[i-1][j-1][k-1]

dp()
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    elif a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = 1')
    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = {dp_array[20][20][20]}')
    else:
        print(f'w({a}, {b}, {c}) = {dp_array[a][b][c]}')