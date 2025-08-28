s = input()
print(len(set(s[j:j+i] for i in range(1, len(s) + 1) for j in range(len(s) - i + 1))))