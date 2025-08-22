def convert(n, q):
    conv_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod < 10: conv_base += str(mod)
        else : conv_base += str(chr(ord('A') + mod - 10))

    return conv_base[::-1]
    # 진수 변환 시 거꾸로 돌리는 것

N, B = map(int, input().split())
print(convert(N, B))