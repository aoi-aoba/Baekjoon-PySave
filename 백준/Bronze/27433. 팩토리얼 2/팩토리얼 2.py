def factorial(n):
    val = 1
    for i in range(2, n + 1):
        val *= i
    return val


import sys
print(factorial(int(sys.stdin.readline())))