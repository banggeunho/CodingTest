# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 16.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 2930 힙.
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



  
      