import sys
input = sys.stdin.readline

n, m = map(int, input().split())
setA = set(input().split())
setB = set(input().split())
print(len((setA - setB).union(setB - setA)))