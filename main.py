# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 18.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

# 1860. 진기의 최고급 붕어빵
for tc in range(1, int(input())+1):
  n, m, k = map(int, input().split())
  cus = list(map(int, input().split()))
  cus.sort()
  total, prev, cnt = 0
  solve = True
  for i in cus:
    if i//m >= 1 and i//m != prev:
      cnt += 1
      total = (i//m)*k-cnt
      prev = i//m

    elif total > 0:
      total -= 1
      cnt += 1

    elif i == 0:
      print(f'#{tc} Impossible')
      solve = False
      break
      
    else:
      print(f'#{tc} Impossible')
      solve = False
      break
        
  if solve:
    print(f'#{tc} Possible')
    
    
  