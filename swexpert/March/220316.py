# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 16.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

# 2930 힙
import heapq

for tc in range(1, int(input())+1):
  heap = []
  answer = []
  n = int(input())
  for i in range(n):
    arr = list(map(int, input().split()))
    if len(arr) > 1:
      heapq.heappush(heap, (-arr[1]))
    else:
      if heap:
        a = heapq.heappop(heap)
        answer.append(-a)
      else:
        answer.append(-1)

  print(f'#{tc} ', end='')
  for i in answer:
    print(i, end=' ')
  print()


# 2948 문자열 교칩합
from bisect import bisect_left, bisect_right

def count_by_range(arr, target):

  left_index = bisect_left(arr, target)
  right_index = bisect_right(arr, target)

  return right_index - left_index

for tc in range(1, int(input())+1):
  n, m = map(int, input().split())
  n_arr = list(input().split())
  m_arr = list(input().split())
  # binary search를 사용하기 위해 정렬
  n_arr.sort()
  m_arr.sort()
  answer = 0

  # 각 배열의 길이를 비교해서 짧은 것으로 선택
  if n > m:
    for i in m_arr:
      if count_by_range(n_arr, i):
        answer += 1

  else:
    for i in n_arr:
      if count_by_range(m_arr, i):
        answer += 1

  print(f'#{tc} {answer}')
  
      