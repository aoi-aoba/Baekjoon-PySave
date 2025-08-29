import sys
input = sys.stdin.readline

def isprime(n):
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

n = int(input())
for _ in range(n):
	t = int(input())
	while True:
		if isprime(t):
			print(t)
			break
		else:
			t += 1