def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

import sys
print(factorial(int(sys.stdin.readline())))