arr = [list(map(int, input().split())) for _ in range(9)]

row_list = [max(data) for data in arr]
row_idx_list = [data.index(max(data)) for data in arr]

print(max(row_list))
print(row_list.index(max(row_list)) + 1, row_idx_list[row_list.index(max(row_list))] + 1)