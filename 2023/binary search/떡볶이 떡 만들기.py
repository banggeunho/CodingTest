# 4 6
# 19 15 10 17

def binary_search(array, target, start, end):
    while start <= end:
        gain = 0
        mid = (start + end) // 2 # divide

        for i in array:
            temp = i - mid
            if temp > 0:
                gain += temp # 손님이 가져갈 수 있는 양

        if target == gain:
            return mid
        # 가져갈 수 있는 떡의 양이 클 경우 -> 절단기 높이를 높여 떡이 더 적어지게 한다.
        elif target < gain:
            start = mid + 1

        # 가져갈 수 있는 떡의 양이 많을 경우 -> 절단기 높이를 낮춰 떡을 더 많이 받을 수 있게 한다.
        else:
            end = mid - 1

    return None # 아무 것도 찾지 못했을 경우


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, max(array))
if result is None:
    print("원소가 존재하지 않습니다.")

else:
    print("절단기 높이 :", result)