import sys
input = sys.stdin.readline

maxVal = -1_000_000_000
minVal = 1_000_000_000

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

def tracker(now, depth):
    if depth == n:
        global maxVal, minVal
        maxVal = max(maxVal, now)
        minVal = min(minVal, now)
        return
    global nums, ops
    for i in range(len(ops)):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                new_num = now + nums[depth]
                tracker(new_num, depth + 1)
            elif i == 1:
                new_num = now - nums[depth]
                tracker(new_num, depth + 1)
            elif i == 2:
                new_num = now * nums[depth]
                tracker(new_num, depth + 1)
            else:
                if now < 0:
                    new_num = -(-1 * now // nums[depth])
                else:
                    new_num = now // nums[depth]
                tracker(new_num, depth + 1)
            ops[i] += 1
            
tracker(nums[0], 1)
print(maxVal)
print(minVal)