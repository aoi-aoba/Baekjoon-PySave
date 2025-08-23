arr = [int(input()) for _ in range(3)]
if sum(arr) != 180: print("Error")
elif arr.count(arr[0]) == 3: print("Equilateral")
elif arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[0]: print("Isosceles")
else: print("Scalene")