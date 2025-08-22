words = []
for _ in range(5):
    word = list(input().rstrip())
    word += ['']*(15-len(word))
    words.append(word)
print(''.join(map(''.join, zip(*words))))