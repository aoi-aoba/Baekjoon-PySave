while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    elif sum(arr)-max(arr) <= max(arr):
        print("Invalid")
    elif arr.count(arr[0]) == 3:
        print("Equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[0]:
        print("Isosceles")
    else:
        print("Scalene")