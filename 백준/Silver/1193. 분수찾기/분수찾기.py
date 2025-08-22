X = int(input())

line = end = 0

while end < X:
    line += 1
    end += line

pos = end - X

if line % 2 == 0:
    a = line - pos
    b = pos + 1
else:
    a = pos + 1
    b = line - pos

print(str(a) + "/" + str(b))