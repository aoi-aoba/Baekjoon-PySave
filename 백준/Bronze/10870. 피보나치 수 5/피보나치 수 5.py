def fibo(n):
    a = b = 1
    if n <= 1:
        return n
    for i in range(1, n):
        a, b = b, b + a
    return a

import sys
print(fibo(int(sys.stdin.readline())))