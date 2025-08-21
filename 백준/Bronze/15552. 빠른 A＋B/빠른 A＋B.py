import sys

T = int(input())
for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)