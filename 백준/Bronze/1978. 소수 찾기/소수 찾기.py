n = int(input())
arr = list(map(int, input().split()))
primeNum = 0
for i in arr:
    if i == 1:
        continue
    isPrime = True
    for j in range(2, int(i**(1/2)) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primeNum += 1
print(primeNum)