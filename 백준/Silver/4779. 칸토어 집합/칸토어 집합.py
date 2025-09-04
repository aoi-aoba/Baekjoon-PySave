def makeBlank(start, n):
    if n == 1:
        return
    for i in range(start + n // 3, start + (n // 3) * 2):
        result[i] = ' '
    makeBlank(start, n // 3)
    makeBlank(start + n // 3 * 2, n // 3)

import sys
while True:
    try:
        N = int(sys.stdin.readline())
        result = ['-'] * (3 ** N)
        makeBlank(0, 3 ** N)
        print(''.join(result))
    except:
        break