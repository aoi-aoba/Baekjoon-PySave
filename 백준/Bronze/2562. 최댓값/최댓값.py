index = maxVal = 0
for i in range(1, 10):
    temp = int(input())
    if maxVal < temp:
        index = i
        maxVal = temp
print(maxVal)
print(index)