MAX_VAL = 123456 * 2

def sieve(n):
    is_prime = [True] * (n + 1)
    end = int(n ** 0.5)
    for i in range(2, end + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

import sys
input = sys.stdin.readline

primes = sieve(MAX_VAL)

while True:
    num = int(input())
    if num == 0:
        break
    print(sum(1 for i in range(num + 1, 2 * num + 1) if primes[i]))