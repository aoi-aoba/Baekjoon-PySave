n = int(input())
arr = list(map(int, input().split()))

def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

primeCnt = sum(1 for num in arr if isprime(num))
print(primeCnt)