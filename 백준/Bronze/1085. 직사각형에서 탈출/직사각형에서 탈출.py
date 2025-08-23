x, y, w, h = map(int, input().split())
arr = [abs(x-w), x, abs(y-h), y]
print(min(arr))