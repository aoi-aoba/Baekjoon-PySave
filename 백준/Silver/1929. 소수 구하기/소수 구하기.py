MAX_VAL = 1000000

def sieve(n):
	arr = [i for i in range(n + 1)]
	end = int(n ** 0.5)
	for i in range(2, end + 1):
		if arr[i] == 0:
			continue
		for j in range(i * i, n + 1, i): # i*i보다 작은 합성수 모두 이미 지워짐
			arr[j] = 0
	return [i for i in arr[2:] if arr[i]]

import sys

primes = set(sieve(MAX_VAL))
input = sys.stdin.readline

m, n = map(int, input().split())
print("\n".join(str(i) for i in range(m, n + 1) if i in primes))