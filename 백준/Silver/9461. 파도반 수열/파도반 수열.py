import sys
input = sys.stdin.readline

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1

for k in range(4, 101):
    dp[k] = dp[k-2] + dp[k-3]

t = int(input())
for _ in range(t):
    print(dp[int(input())])