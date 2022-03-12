# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 12.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

##### (Case 1) Bisect를 이용하여 문제 풀이 #######
from bisect import bisect_left, bisect_right
def countNum(arr, a):
  left = bisect_left(arr, a)
  right = bisect_right(arr, a)

  if right-left == 0:
    return -1
    
  return right - left

n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(countNum(arr, x))

  
##### (Case 2) 이진탐색 함수 작성하여 문제 풀이 #######    

def count_by_value(arr, x):
  n = len(arr)
  a = first(arr, x, 0, n-1)

  if a == None:
    return 0

  b = last(arr, x, 0, n-1)

  return b-a+1

def first(array, target, start, end):
  if start > end:
    return None

  mid = (start+end) // 2

  # and 앞의 구문을 통해 가장 왼쪽에 있는지 확인 가능
  if (mid ==0 or array[mid - 1] < target) and array[mid] == target:
    return mid

  # 같은 수가 중복되서 나올 수 있어 등호(=)를 넣어준다.
  elif array[mid] >= target:
    return first(array, target, start, mid - 1)

  else:
    return first(array, target, mid + 1, end)


def last(array, target, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if (mid == n-1 or array[mid + 1] > target) and array[mid] == target:
    return mid

  elif array[mid] > target:
    return last(array, target, start, mid - 1)

  else:
    return last(array, target, mid + 1, end)

n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = count_by_value(arr, x)
if  count == 0:
  print(-1)

else:
  print(count)