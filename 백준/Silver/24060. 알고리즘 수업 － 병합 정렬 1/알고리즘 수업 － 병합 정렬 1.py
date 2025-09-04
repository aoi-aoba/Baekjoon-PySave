import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
res = -1

def merge(arr, srt, mid, end):
    i = srt
    j = mid + 1
    t = 0
    tmp = []

    global cnt, res

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= end:
        tmp.append(arr[j])
        j += 1

    i, t = srt, 0
    while i <= end:
        arr[i] = tmp[t]
        cnt += 1
        if cnt == K:
            res = arr[i]
            break
        i, t = i + 1, t + 1

def merge_sort(arr, srt, end):
    if srt < end:
        mid = (srt + end) // 2
        merge_sort(arr, srt, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, srt, mid, end)
    return arr

merge_sort(arr, 0, N - 1)
print(res)