import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 중복 제거 후 정렬
sortArr = sorted(set(arr))

# enumerate로 (인덱스, 값) 쌍 만들고 value:idx 형태로 매핑 dictionary 만듦
rank = {value : idx for idx, value in enumerate(sortArr)}

# arr 리스트 key 값 x에 대하여 rank 접근
print(" ".join(str(rank[x]) for x in arr))