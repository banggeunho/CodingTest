# 10 7
# 1 3 5 7 9 11 13 15 17 19

def binary_search(array, target, start, end):

    if start > end:
        return None

    mid = (start+end) // 2

    if array[mid] == target:
        return mid;

    elif array[mid] > target: # 타겟 값이 중간점보다 작으면은
        return binary_search(array, target, start, mid-1)

    else: # 타겟 값이 중간점보다 크면
        return binary_search(array, target, mid+1, end)


n, target = map(int, input().split())

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result is None:
    print("원소가 존재하지 않습니다.")

else:
    print("찾고자 하는 값의 인덱스 :", result)