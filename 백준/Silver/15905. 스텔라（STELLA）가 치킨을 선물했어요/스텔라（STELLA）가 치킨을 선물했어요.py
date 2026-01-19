n = int(input())
lst = []

for i in range(n):
    info = [int(i) for i in input().split()]
    lst.append([info[0], info[1]])

lst.sort(key= lambda x : (x[0], -x[1]), reverse=True)

cnt = 0
for i in range(5, len(lst)):
    if lst[i][0] == lst[4][0]:
        cnt += 1

print(cnt)