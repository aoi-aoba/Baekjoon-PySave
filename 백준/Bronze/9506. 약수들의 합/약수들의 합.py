while True:
    n = int(input())
    if n == -1:
        break

    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)

    if n == sum(lst):
        print(str(n) + " = " + " + ".join(str(i) for i in lst))
    else:
        print("%d is NOT perfect." % n)