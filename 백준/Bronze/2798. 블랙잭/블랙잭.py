n, m = map(int, input().split())
cards = list(map(int, input().split()))
maxThree = 0
for i in range(0, len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            sumCards = cards[i] + cards[j] + cards[k]
            if maxThree < sumCards <= m :
                maxThree = sumCards
print(maxThree)