import sys

num1 = 0
num2 = 1
n = int(sys.stdin.readline())
for i in range(n + 1):
    num1, num2 = num1 + num2, num1
print(num2)