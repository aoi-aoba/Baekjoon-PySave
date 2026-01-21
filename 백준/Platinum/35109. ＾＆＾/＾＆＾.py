import sys
input = sys.stdin.readline

def solve(n):
    if n == '10':
        return '0'
    elif str(n).count('0') == 1 and str(n)[len(n)-1] == '0':
        return '1' * (len(n) - 2) + '00'
    elif str(n).count('0') >= 2 and str(n)[len(n)-1] == '0':
        return '1' * len(n)
    else:
        return n

print(solve(input().rstrip()))