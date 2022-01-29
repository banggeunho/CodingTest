# 코딩테스트 대비 기초 문제 풀이 13일차
# Date : 2022. 01. 30.
# 정렬(Sorting) // 다양한 정렬 알고리즘 공부 및 간단 구현


# 정렬(Sorting)이란? 데이터를 특정한 기준에 따라서 순서대로 나열하는 것.
# 선택정렬, 삽입 정렬, 퀵 정렬, 계수 정렬

# 1. 선택정렬(Selection Sort) : 가장 작은데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해
#                              앞에서 두 번째와 바꾸는 과정을 반복
# - 가장 원시적인 방법, '가장 작은 것을 선택한다.'
# 시간복잡도 : O(N^2) / N+(N-1)+(N-2)+...+2

# 예제코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selectionSort(array):
  # 첫번째 부터 마지막까지 한번씩 살펴본다.
  for i in range(len(array)):
    min_index = i

    # 기준으로 정한 것 뒤부터 끝까지 비교하여 제일 작은 값의 인덱스를 찾아낸다.
    for j in range(i+1, len(array)):
      if array[min_index] > array[j]:
        min_index = j

    # 제일 작은 값의 인덱스값과 현재 기준의 인덱스의 값을 바꿔준다
    # 파이썬에서는 별도의 임시 저장 변수가 없어도 swap이 가능하다.
    array[i], array[min_index] = array[min_index], array[i]

  print('Selection Sorting', array)

selectionSort(array)

# 2. 삽입정렬(Insertion Sort) : 특정한 데이터를 적절한 위치에 '삽입'하는 정렬 알고리즘
# - 삽입정렬은 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬 되어 있을 때' 훨씬 효율적이다.
# - 삽입정렬은 두 번째 데이터부터 시작한다. (첫 번째 데이터는 그 자체로 정렬되어 있다고 판단)
# 시간복잡도 : O(N^2) / 거의 정렬되어 있는 리스트 데이터에서는 최선의 경우 O(N).

# 예제코드
def insertionSort(array):
  # 두 번째 데이터부터 마지막까지 기준을 한 번씩 잡는다.
  for i in range(1, len(array)):
    # 자기자신부터 시작하여 자기 이전의 데이터 보다 큰 수가 있으면 SWAP한다.
    # 큰 수가 없으면 BREAK 한다. (자기 자신 이전의 데이터들은 오름차순으로 정렬되어있기 때문이다.)
    for j in range(i, 0, -1):
      if array[j] < array[j-1]:
        array[j], array[j-1] = array[j-1], array[j]
      else:
        break
  print('Insertion Sorting', array)

insertionSort(array)


# 위에서 아래로 문제 (예제)
n = int(input())
arr = list()
for i in range(n):
  arr.append(int(input()))

arr = sorted(arr, reverse=True)

for i in(arr):
  print(i, end=' ')

print('')

# 성적이 낮은 순서로 학생 출력하기
n = int(input())
arr = []
for i in range(n):
  input_data = input().split()
  # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  arr.append( (input_data[0], int(input_data[1])) )

# 키(key)를 이용하여, 점수를 기준으로 정렬
arr = sorted(arr, key=lambda x: x[1])

# 정렬이 수행된 결과를 출력
for student in arr:
  print(student[0], end=' ')
