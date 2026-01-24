import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [set() for _ in range(N + 1)]

def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = deque([start])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    return sum(dist[1:])

for _ in range(M):
    data = list(map(int, input().split()))
    k = data[0]
    cows = data[1:]

    for i in range(k):
        for j in range(i + 1, k):
            a, b = cows[i], cows[j]
            graph[a].add(b)
            graph[b].add(a)

min_avg = float('inf')
for cow in range(1, N + 1):
    total_dist = bfs(cow)
    avg = total_dist / (N - 1)
    min_avg = min(min_avg, avg)

print(int(min_avg * 100))