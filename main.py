# 코딩테스트 대비 기초 문제 풀이 36일차
# Date : 2022. 02. 24.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 5215 햄버거 다이어트
from itertools import combinations
for tc in range(1, int(input())+1):

  n, l = map(int, input().split())
  taste = []
  kcal = []
  max_taste = 0
  for i in range(n):
    a, b = map(int, input().split())
    kcal.append((b,a))

  for i in range(1, n+1):
    for j in list(combinations(kcal, i)):
      total_kcal = 0
      total_taste = 0
      for k in range(len(j)):
        total_kcal += j[k][0]
        total_taste += j[k][1]

      if total_kcal <= l:
        max_taste = max(max_taste, total_taste)
            

  print(f'#{tc} {max_taste}')
    

