# 코딩테스트 대비 기초 문제 풀이 15일차
# Date : 2022. 02. 02.
# 순차 탐색, 이진 탐색에 대한 원리 공부 및 파이썬 코드로 구현


# 순차 탐색(Sequential Search)이란 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.
# 시간 복잡도 : Worst-Case -> O(N) // 하나씩 확인해야 하기 때문에

# 순차 탐색 소스코드
def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i+1

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))


# 이진 탐색(Binary Search) : 반으로 쪼개면서 탐색하기
# 시작점, 끝점, 그리고 중간점의 위치를 나타내는 변수 3개를 사용
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
# 시간 복잡도 : O(logN) // 절반씩 데이터를 줄어들도록 만든다는 점은 퀵 정렬과 공통점이 있다.

# 재귀 함수를 이용한 이진 탐색 구현

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2

  # 찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  if target < array[mid]:
    return binary_search(array, target, start, mid-1)
  
  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, target, mid+1, end)


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
  print('원소가 존재하지 않습니다.')

else:
  print(result+1)

# 반복문을 이용한 이진 탐색 구현

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid

    elif array[mid] > target:
      end = mid - 1
    
    else:
      start = mid + 1
  
  return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
  print('원소가 존재하지 않습니다.')

else:
  print(result+1)


# 이진 탐색 트리 ( 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드 )
# 빠르게 입력 받기 : 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
# 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 이진 탐색 알고리즘을 의심!!
# sys 라이브러리의 readline() 함수를 이용하여 시간 초과를 피할 수 있다.

import sys

# rstrip()은 엔터키를 지워 주는 것
input_data = sys.stdin.readline().rstrip()


# 부품 찾기 문제 (이진 탐색 이용)
n = int(input())
item = list(map(int, input().split()))

# 이진 탐색을 수행하기 위해 사전에 정렬 수행
item.sort()

m = int(input())
search_item = list(map(int, input().split()))

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2

  # 찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  if target < array[mid]:
    return binary_search(array, target, start, mid-1)
  
  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, target, mid+1, end)

for s_item in search_item:

  result = binary_search(item, s_item, 0, n - 1)

  if result == None:
    print('no', end=' ')
  
  else:
    print('yes', end=' ')

# 부품 찾기 문제(계수정렬 이용)

# 부품 찾기 문제
n = int(input())
# 최대 부품 갯수가 100만개 이기 떄문
array = [0]*1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)] += 1

# 손님이 요청한 부품 개수 입력
m = int(input())

# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
search_item = list(map(int, input().split()))

for item in search_item:

  if array[item] > 0:
    print('yes', end=' ')
  else:
    print('no', end=' ')

# 부품 찾기 문제( 집합 자료형 이용 )
# 이 문제는 단순히 특정한 수가 한 번이라도 등장했는지 검사하면 되므로 집합 자료형을 이용해서 문제를 해결 가능
# set() 함수는 집합자료형을 초기화할 때 사용한다.
# 이러한 집합자료형은 단순히 특정한 데이터가 존재하는지 검사할 때에 매우 효과적으로 사용할 수 있다.

n = int(input())
array = set(map(int, input().split()))
print(array)
m = int(input())
x = list(map(int, input().split()))


for i in x:
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end = ' ')


# 떡볶이 떡 만들기
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
  total = 0
  mid = (start + end) // 2

  # 잘린 떡의 길이 계산
  for i in array:

    # 잘르는 점이 떡의 길이보다 작을때 더한다.
    if i > mid:
      total += i - mid

  # 잘린 떡의 길이가 손님이 요청한 떡보다 짧을 경우
  if total < m:
    end = mid - 1

  # 잘린 떡의 길이가 손님이 요청한 떡보다 길 경우
  else:
    start = mid + 1 # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
    result = mid
    
print(result)

