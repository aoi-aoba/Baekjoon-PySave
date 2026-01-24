import sys
input = sys.stdin.readline

day = {'MON':0, 'TUE':1, 'WED':2, 'THU':3, 'FRI':4}

N, M = map(int, input().split())
credit = [0] * N
lectures = [[] for _ in range(N)]

for i in range(N):
    lecture_info = input().split()
    credit[i] = int(lecture_info[0])
    s = int(lecture_info[1])

    for j in range(s):
        day_idx = day[lecture_info[2+2*j]]
        hour = int(lecture_info[2+2*j+1])
        lectures[i].append((day_idx, hour))

tot_masks = 1 << N # 강의 선택여부의 전체집합 원소 수
for mask in range(tot_masks):
    used = [[0] * 24 for _ in range(5)]
    sumCredit, conflict = 0, 0
    for i in range(N):
        # 해당 mask가 i번째를 선택하는지 판독 후 학점에 합산
        if not (mask & (1 << i)):
            continue
        sumCredit += credit[i]
        # 이미 쓰인 시간이면 충돌이 있는 것이므로 제외
        for lec in lectures[i]:
            d, h = lec
            if used[d][h]:
                conflict = 1
                break
            used[d][h] = 1
        if conflict: break
    # 충돌 없이 학점 만족하면 바로 종료
    if not conflict and sumCredit >= M:
        print('YES')
        exit(0)
print('NO')