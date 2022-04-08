
# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 04. 3.
# 삼성전자 기출 문제
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

# 우선순위 큐 구현 문제
import heapq
q = []
n = int(input())
answer = []
for i in range(n):
  data = int(input())
  if data == 0:
    if len(q) < 1:
      heapq.heappush(q, data)
    answer.append(heapq.heappop(q))
  else:
    heapq.heappush(q, data)

for i in answer:
  print(i)
            