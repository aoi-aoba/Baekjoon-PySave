n = int(input())
cnt = 0

while n != 0:
    if n % 5 == 0:
        n -= 5
        cnt += 1
    elif n % 2 == 0:
        n -= 2
        cnt += 1
    elif n > 5:
        n -= 5
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)