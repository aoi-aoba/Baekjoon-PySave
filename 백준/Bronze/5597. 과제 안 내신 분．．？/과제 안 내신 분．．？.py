def solve():
    arr = []
    for i in range(28) :
        arr.append(int(input()))

    for i in range(1, 31) :
        if arr.count(i) == 0:
            print(i)

solve()