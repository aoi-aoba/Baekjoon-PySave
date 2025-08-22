arr = list(map(int, input().split()))
if arr[0] < arr[1] : ascend = True; descend = False
else : descend = True; ascend = False;
for i in range(2, 8):
    if ascend and arr[i] < arr[i-1]:
        ascend = False; break
    if descend and arr[i] > arr[i-1]:
        descend = False; break
print("ascending" if ascend else "descending" if descend else "mixed")