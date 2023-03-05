n = int(input())

arr = list(map(int, input().split()))


def search_fixed_point(arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid

    elif arr[mid] < mid:
        return search_fixed_point(arr, mid + 1, end)

    else:
        return search_fixed_point(arr, start, mid - 1)

print(search_fixed_point(arr, 0, n-1))