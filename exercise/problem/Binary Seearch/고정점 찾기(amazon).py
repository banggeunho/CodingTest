# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 12.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 고정점 찾기 (Amazon 인터뷰)

def search_fixed_point(arr, start, end):
  if start > end:
    return -1

  mid = (start + end) // 2

  # 고정점일 경우 return
  if arr[mid] == mid:
    return mid

  # 중간값 인덱스가 중간값보다 작으면 정렬된 수이기 때문에 오른쪽에는 고정점이 없음
  elif arr[mid] > mid:
    return search_fixed_point(arr, start, mid - 1)

  else:
    return search_fixed_point(arr, mid + 1, end)

n = int(input())
arr = list(map(int, input().split()))

fixed_point = search_fixed_point(arr, 0, n-1)
print(fixed_point)