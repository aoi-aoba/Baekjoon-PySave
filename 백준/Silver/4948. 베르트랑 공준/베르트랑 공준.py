MAX_VAL = 123456 * 2

def sieve(n):
    arr = [i for i in range(n + 1)]
    end = int(n ** 0.5)
    for i in range(2, end + 1):
        if arr[i] == 0:
            continue
        for j in range(i * i, n + 1, i):
            arr[j] = 0
    return set(i for i in arr[2:] if arr[i] != 0)

import sys
input = sys.stdin.readline

primes = sieve(MAX_VAL)
num = int(input())
while num != 0:
    print(sum(1 for i in range(num + 1, 2 * num + 1) if i in primes))
    num = int(input())
