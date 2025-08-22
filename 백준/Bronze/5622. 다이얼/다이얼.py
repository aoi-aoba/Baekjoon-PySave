word = input()
res = 0

for i in word:
    if "ABC".find(i) != -1 : res += 3
    elif "DEF".find(i) != -1 : res += 4
    elif "GHI".find(i) != -1 : res += 5
    elif "JKL".find(i) != -1 : res += 6
    elif "MNO".find(i) != -1 : res += 7
    elif "PQRS".find(i) != -1 : res += 8
    elif "TUV".find(i) != -1 : res += 9
    elif "WXYZ".find(i) != -1 : res += 10

print(res)