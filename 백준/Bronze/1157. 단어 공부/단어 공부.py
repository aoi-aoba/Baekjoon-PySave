s = input().strip().lower()
alphaCnt = [0] * 26

for let in s:
    alphaCnt[ord(let) - ord('a')] += 1

maxCnt = max(alphaCnt)
if alphaCnt.count(maxCnt) > 1:
    print("?")
else:
    print(chr(alphaCnt.index(maxCnt) + ord('A')))
