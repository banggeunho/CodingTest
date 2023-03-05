from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_value = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_value

n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = count_by_range(arr, x, x)
if result == 0:
    print(-1)
else:
    print(result)

