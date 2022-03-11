# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 11.
# Sorting
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 백준 1715
# 카드 정렬하기
# 우선순위 큐(heapq)를 사용하면 넣고 꺼낼때 자동적으로 낮은 것 부터 꺼내와서
# 자동적으로 정렬을 수행~ 오름차순을 하기 위해선 별도의 장치가 필요하다.

import heapq
n = int(input())
#힙(heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
  heapq.heappush(heap, int(input()))
result = 0
# 힙에 원소가 1개 남을때 까지
while len(heap) != 1:
  # 가장 작은 2개의 카드 묶음 꺼내기
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  sum_value = one+two
  # 다시 삽입
  heapq.heappush(heap, sum_value)
  result += sum_value
print(result)




  
    
    