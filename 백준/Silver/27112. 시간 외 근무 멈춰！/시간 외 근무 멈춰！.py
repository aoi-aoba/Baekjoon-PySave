import sys
input = sys.stdin.readline

def holiday(start, end):
    cnt = 0
    for i in range(start, end + 1):
        if i % 7 == 6 or i % 7 == 0:
            cnt += 1
    return cnt

n = int(input())
works = [tuple(map(int, input().split())) for _ in range(n)]
works.sort(key=lambda x: x[0])

over, work, now = 0, 0, 0
for i in range(n):
    day = works[i][0]
    work += day - now - holiday(now + 1, day)
    now = day
    work -= works[i][1]
    if work < 0:
        over += abs(work)
        work = 0
    if over > now:
        over = -1
        break
print(over)