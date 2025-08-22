n = input()
isPal = True
for i in range(len(n) // 2):
    if n[-(i+1)] != n[i]:
        isPal = False; break
print(1 if isPal else 0)