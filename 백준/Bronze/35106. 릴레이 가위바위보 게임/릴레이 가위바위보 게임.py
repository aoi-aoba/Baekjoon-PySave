n = input()
lst = map(int, input().split())
cnt = [0, 0, 0, 0]

for i in lst:
    cnt[i] += 1

maxval, minval = max(cnt), min(cnt[1:4])
res = ['0', '0']

for i in range(1, 4):
    if cnt[i] == maxval:
        res[1] = str(i)
    if cnt[i] == minval:
        res[0] = str(i)

print("\n".join(res))