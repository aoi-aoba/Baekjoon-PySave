n = int(input())
t = int(input())
hand_num = [int(i) for i in input().split()]
fail_num = [int(i) for i in input().split()]
res = []
chk = set()

for target in fail_num:
    target %= len(hand_num)
    if target == 0:
        target = len(hand_num)
    for _ in range(target - 1):
        hand_num.insert(len(hand_num), hand_num.pop(0))
    res += [str(hand_num[0])]

print(' '.join(res))

