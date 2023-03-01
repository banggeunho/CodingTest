# 10 7
# 1 3 5 7 9 11 13 15 17 19

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 # divide

        if array[mid] == target: # 중간 값과 타겟 값이 같을 경우
            return mid

        elif array[mid] > target: # 타겟 값이 중간 값 보다 작을 경우
            end = mid - 1

        else: # 타겟 값이 중간 값 보다 클 경우
            start = mid + 1

    return None # 아무 것도 찾지 못했을 경우


n, target = map(int, input().split())

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result is None:
    print("원소가 존재하지 않습니다.")

else:
    print("찾고자 하는 값의 인덱스 :", result)