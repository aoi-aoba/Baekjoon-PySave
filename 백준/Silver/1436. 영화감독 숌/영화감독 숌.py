n = int(input())
num = 666
idx = 1
while idx != n:
    num += 1
    if str(num).count("666") > 0:
        idx += 1
print(num)