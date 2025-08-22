tar = int(input())
n = int(input())
val = 0
for i in range(n):
    price, num = map(int, input().split())
    val += price * num
print("Yes" if tar == val else "No")