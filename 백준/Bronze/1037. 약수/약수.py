import sys
input = sys.stdin.readline

n = input()
numArr = list(map(int, input().split()))
print(max(numArr) * min(numArr))