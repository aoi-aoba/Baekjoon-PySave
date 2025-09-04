import sys
input = sys.stdin.readline

def tracker(n):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return

    for i in range(n, N+1):
        if i not in res:
            res.append(i)
            tracker(i)
            res.pop()

N, M = map(int, input().split())
res = []

tracker(1)