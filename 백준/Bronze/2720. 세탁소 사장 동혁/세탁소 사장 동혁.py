def solve(charge):
    arr = [0] * 4
    if charge >= 25:
        arr[0] = charge // 25
        charge %= 25
    if charge >= 10:
        arr[1] = charge // 10
        charge %= 10
    if charge >= 5:
        arr[2] = charge // 5
        charge %= 5
    arr[3] = charge
    print(*arr)

T = int(input())
for _ in range(T):
    solve(int(input()))