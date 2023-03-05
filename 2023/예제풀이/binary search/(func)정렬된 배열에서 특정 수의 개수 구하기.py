def count_by_range(a, left_value, right_value):
    left_value = bisect_left(a, left_value, 0, len(a)-1)

    if left_value is None:
        return 0

    right_index = bisect_right(a, right_value, 0, len(a)-1)
    return right_index - left_value + 1


def bisect_left(arr, target, start, end):

    if start > end:
        return None

    mid = (start+end) // 2

    if (mid == 0 or arr[mid-1] < target) and arr[mid] == target:
        return mid

    elif arr[mid] >= target:
        return bisect_left(arr, target, start, mid - 1)

    else:
        return bisect_left(arr, target, mid + 1, end)


def bisect_right(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == n-1 or target < arr[mid + 1]) and arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return bisect_right(arr, target, start, mid - 1)

    else:
        return bisect_right(arr, target, mid + 1, end)


n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = count_by_range(arr, x, x)
if result == 0:
    print(-1)
else:
    print(result)

