MAX_VAL = 1_000_000

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    end = int(n ** 0.5)
    for i in range(2, end + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

import sys
input = sys.stdin.readline

result = []
primes = sieve(MAX_VAL)
t = int(input())

for _ in range(t):
    tar = int(input())
    cnt = sum(1 for i in range(2, tar // 2 + 1) if primes[i] and primes[tar - i])
    result.append(str(cnt))

print('\n'.join(result))