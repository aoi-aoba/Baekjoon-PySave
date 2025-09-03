import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

print(round(sum(arr) / n))  # 산술평균
print(arr[n // 2])          # 중앙값

counter = Counter(arr)
modes = counter.most_common(2)

if len(modes) == 1:
    print(modes[0][0])
elif modes[0][1] == modes[1][1]:
    print(modes[1][0])
else:
    print(modes[0][0])
# 최빈값

print(max(arr) - min(arr))  # 범위