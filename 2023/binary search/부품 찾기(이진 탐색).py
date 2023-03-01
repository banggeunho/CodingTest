n = int(input())
stores = list(map(int, input().split()))
stores.sort() # 정렬 (이진 탐색을 위한)

m = int(input())
finds = list(map(int, input().split()))

def binary_search(array, target, start, end):

    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return target

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)

for find in finds:
    if binary_search(stores, find, 0, n-1) is None:
        print('no', end= ' ')
    else:
        print('yes', end = ' ')