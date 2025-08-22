n = int(input())
route = cnt = 1
while n > route:
    route += 6 * cnt
    cnt += 1
print(cnt)