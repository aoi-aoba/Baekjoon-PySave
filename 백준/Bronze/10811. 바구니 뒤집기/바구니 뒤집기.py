n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    temp = arr[i-1 : j]
    temp.reverse()
    arr[i-1 : j] = temp
print(*arr)