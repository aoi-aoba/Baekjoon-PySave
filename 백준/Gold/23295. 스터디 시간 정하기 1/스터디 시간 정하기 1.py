import sys
input = sys.stdin.readline

n, t = map(int, input().split())
diff = [0] * 100001
maxLimit = 0

for _ in range(n):
    k = int(input())
    for _ in range(k):
        start, end = map(int, input().split())
        maxLimit = max(maxLimit, end)
        diff[start] += 1
        diff[end] -= 1

timeTable = [0] * (maxLimit + 1)
cur_cnt = 0
for i in range(maxLimit):
    cur_cnt += diff[i]
    timeTable[i] = cur_cnt

prefixSum = [0] * (maxLimit + 1)
for i in range(maxLimit):
    prefixSum[i + 1] = prefixSum[i] + timeTable[i]

maxSatisfied = -1
ans = 0

for i in range(maxLimit - t + 1):
    cur = prefixSum[i + t] - prefixSum[i]
    if cur > maxSatisfied:
        maxSatisfied = cur
        ans = i

print(ans, ans + t)