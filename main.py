# 코딩테스트 대비 기초 문제 풀이 14일차
# Date : 2022. 01. 30.
# 정렬(Sorting) // 다양한 정렬 알고리즘 공부 및 간단 구현



# 1. 퀵 정렬(Quick Sort) : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬 알고리즘
# - 기준(Pivot)을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
# - 정렬을 수행하기 전에는 피벗을 어떻게 설정할 것인지 미리 명시해야 한다.
# - 정렬 알고리즘 중에 병합정렬과 같ㅌ이 가장 많이 사용되는 알고리즘
# - 호어 분할방식(Hoare Partition) 기준으로 퀵 정렬을 설명하였음.
# - 시간복잡도 : O(NlogN) // 분할이 이루어져서 정렬을 하기 때문에, 최악의 경우 시간 복잡도가 O(N^2)
# 무작위로 입력되는 경우 빠르게 돌아갈 확률이 높다. BUT 이미 정렬되어 있는 경우 매우 느리게 동작한다.

# 예제코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  # 원소가 1개인 경우 정렬이 완료되었다고 간주하고, 종료
  if start >= end:
    return

  pivot = start
  left = start + 1
  right = end
  while left <= right:

    # 피벗보다 큰 데이터를 찾을 때까지 반복  
    while left <= end and  array[left] <= array[pivot]:
      left += 1
  
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] <= array[pivot]:
      right -= 1

    # left와 right가 엇갈린다면 pivot과 작은 값(오른쪽 값)을 교체
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]

    # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    else:
      array[left], array[right] = array[right], array[left]

  # 분할(divide) 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)
  print(array)

quick_sort(array, 0, len(array)-1)


