import sys
input = sys.stdin.readline

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
ab1 = a1 * b2 + a2 * b1
ab2 = a2 * b2
abGcd = gcd(ab1, ab2)
print(ab1 // abGcd, ab2 // abGcd)