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
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

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
    while right > start and array[right] >= array[pivot]:
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


quick_sort(arr, 0, len(arr)-1)
print(arr)

# 파이썬의 장점을 살린 퀵 정렬 소스코드

def quick_sort(array):
  # 리스트 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array

  pivot = array[0] # 피벗은 첫 번째 리스트
  tail = array[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))


# 2. 게수 정렬(Count Sort) : 특정한 조건이 부합할 때만 사용할 수 있지만 매운 빠른 정렬 알고리즘
# - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
# - 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 너무 크면 계수 정렬을 사용할 수 없음
# - ---> 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 하기 때문
# - 계수 정렬은 비교 기반의 정렬 알고리즘이 아니다.
# - 데이터가 0 과 999,999 단 2개만 존재한다고 가정하면, 리스트의 크기가 100만 개가 되도록 선언해야 함
# - 따라서 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다.
# ----> 데이터의 특성을 파악하기 어렵다면 퀵 정렬을 이용하는 것이 유리하다.
# - 시간복잡도 : O(N+K)


# 예제코드
arr1 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def countSort(array):
  # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
  count = [0] * (max(array) + 1)

  for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터의 해당하는 인덱스의 값 증가

  for i in range(len(count)):
    for j in range(count[i]):
      print(i, end=' ')

countSort(arr1)
print('')

# 파이썬 기본 정렬 함수
# 예제코드
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

result = sorted(arr)
print(result)

arr.sort()
print(arr)

# key 값을 정하여 리스트가 튜플로 구성 되어있을 경우 데이터의 기준을 정할 수 있음.

array = [('바나나',2),('사과', 5), ('딩근', 3)]

def setting(data):
  return data[1]

result = sorted(array, key=setting)
print(result)

# 성적이 낮은 순서로 학생 출력하기 문제를 계수 정렬을 이용하여 풀어보기
n = int(input())
arr = []
for i in range(n):
  input_data = input().split()
  # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  arr.append( (input_data[0], int(input_data[1])) )

array = [i[1] for i in arr]

def a_countSort(array):
  # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
  count = [0] * (max(array) + 1)

  for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터의 해당하는 인덱스의 값 증가

  for i in range(len(count)):
    if count[i] < 1:
      continue
    for j in range(count[i]):
      print(arr[array.index(i)][0], end=' ')

a_countSort(array)


# 두 배열의 원소 교체
import time
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

start_time = time.time()
for i in range(k):
  a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]

print(sum(a))
print('time:', time.time() - start_time)


# 책 풀이

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
start_time = time.time()
a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
print('time:', time.time() - start_time)