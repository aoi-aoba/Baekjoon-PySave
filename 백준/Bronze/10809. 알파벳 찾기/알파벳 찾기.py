arr = []
target = input()

for i in range(26):
    try:
        arr.append(target.index(chr(ord('a') + i)))
    except ValueError:
        arr.append(-1)

print(*arr)