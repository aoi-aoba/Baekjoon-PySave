import sys
input = sys.stdin.readline

def tracker():
    if len(res) == M:
        print(' '.join(map(str, res)))
        return

    for i in range(1, N+1):
        res.append(i)
        tracker()
        res.pop()

N, M = map(int, input().split())
res = []

tracker()