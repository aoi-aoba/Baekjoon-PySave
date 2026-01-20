import sys
input = sys.stdin.readline

single_map = {
    '@': 'a', '[': 'c', '!': 'i',
    ';': 'j', '^': 'n', '0': 'o', '7': 't'
}

N = int(input())
ans = []

for _ in range(N):
    s = input().rstrip()
    result = ""
    replaced_count = 0

    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i] == '\\' and s[i+1] == '\\' and s[i+2] == "'":
            result += 'w'
            replaced_count += 1
            i += 3
        elif i + 1 < len(s) and s[i] == '\\' and s[i+1] == "'":
            result += 'v'
            replaced_count += 1
            i += 2
        else:
            ch = s[i]
            if ch in single_map:
                result += single_map[ch]
                replaced_count += 1
            else:
                result += ch
            i += 1

    if replaced_count * 2 >= len(result):
        ans += ["I don't understand"]
    else:
        ans += [result]

print('\n'.join(ans))