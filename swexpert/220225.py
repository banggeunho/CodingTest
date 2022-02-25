# 코딩테스트 대비 기초 문제 풀이 36일차
# Date : 2022. 02. 24.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 5431. 민석이의 과자 체크하기
for tc in range(1, int(input())+1):
  n, k = map(int, input().split())
  arr = [i for i in range(1, n+1)]
  send = list(map(int, input().split()))
  for i in range(k):
    arr.remove(send[i])

  print(f'#{tc}', end=' ')
  arr.sort()
  for i in arr:
    print(i, end= ' ')

  print()
    

# 5356. 의석이의 세로로 말해요
for tc in range(1, int(input())+1):
  str = []
  for i in range(5):
    str.append(list(input()))

  print(f'#{tc} ', end='')
  for i in range(15):
    for j in range(len(str)):
      if len(str[j]) < i+1:
        continue
      print(str[j][i], end='')

  print()

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


# 5162. 두가지 빵의 딜레마
for tc in range(1, int(input())+1):

  a, b, c = map(int, input().split())
  if a == b:
    print(f'{tc} {c // a}')
  else:
    min_cost = min(a, b)
    print(f'#{tc} {c // min_cost}')


# 4789. 성공적인 공연 기획
for tc in range(1, int(input())+1):
  str = input()
  cur = 0
  answer = 0
  for i in range(len(str)):
    if cur >= i:
      cur += int(str[i])

    else:
      answer += i-cur
      cur += i-cur + int(str[i])

  print(f'#{tc} {answer}')

# 4698 테네스의 특별한 소수
import math
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
  
prime = [i for i in range(2, 1000001) if is_prime_number(i)]

for tc in range(1, int(input())+1):
  d, a, b = map(int, input().split())
  cnt = 0

  for i in prime:
    if a > i:
      continue
      
    elif i > b:
      break

    else:
      if str(d) in str(i):
        cnt += 1
        
  print(f'#{tc} {cnt}')