def solve():
    n = int(input())
    arr = input().split()
    v = int(input())
    ans = 0

    for i in arr :
        if int(i) == v:
           ans += 1

    print(ans)

solve()