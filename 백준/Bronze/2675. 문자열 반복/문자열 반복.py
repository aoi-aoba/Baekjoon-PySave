T = int(input())
for t in range(T):
    rep, tar = map(str, input().split())
    for i in tar:
        print(i * int(rep), end='')
    print()