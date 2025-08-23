def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

primes = [num for num in range(int(input()), int(input()) + 1) if isprime(num)]

if len(primes) == 0:
    print(-1)
else :
    print(sum(primes))
    print(min(primes))