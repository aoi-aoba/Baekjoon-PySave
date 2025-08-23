arr = list(map(int, input().split()))
val = sum(arr) - max(arr)
print(2 * val - 1 if val <= max(arr) else sum(arr))