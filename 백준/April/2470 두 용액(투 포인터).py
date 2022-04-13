# 투포인터 문제
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n - 1
result = []
temp = int(1e10)
while left < right:
    s_left = arr[left]
    s_right = arr[right]
    total = s_left + s_right
    if abs(total) < abs(temp): # 0부터 거리 비교 (교체)
        temp = total
        result = [s_left, s_right]

    if total < 0: #음수면 왼쪽 인덱스를 늘린다
        left += 1
    else: #양수면 오른쪽 인덱스를 늘려준다.
        right -= 1

print(result[0], result[1])