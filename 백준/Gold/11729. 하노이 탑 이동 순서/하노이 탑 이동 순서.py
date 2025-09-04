def hanoi(n, start, via, dest):
    if n == 1:
        print(start, dest)
    else:
        hanoi(n - 1, start, dest, via)
        print(start, dest)
        hanoi(n - 1, via, start, dest)

import sys
n = int(sys.stdin.readline())
print(2 ** n - 1)
hanoi(n, 1, 2, 3)