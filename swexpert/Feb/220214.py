# 코딩테스트 대비 기초 문제 풀이 27일차
# Date : 2022. 02. 13.
# 그리디 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 11285. 다트 게임

import math
for tc in range(1, int(input())+1):
  n = int(input())

  s = []
  r = [20 * i for i in range(1, 11)]
  result = 0

  for i in range(n):
    x, y = map(int, input().split())
    r.append(math.sqrt(pow(x, 2) + pow(y, 2)))
    r.sort()
    idx = r.index(math.sqrt(pow(x, 2) + pow(y, 2)))
    result += 11-r[idx+1]/20
    r.pop(idx)

  print(f'#{tc} {result}')


# 10804 문자열의 거울상

for tc in range(1, int(input())+1):
  str = list(input())
  str.reverse()
  for i in range(len(str)):
    if str[i] == 'q':
      str[i] = 'p'
    elif str[i] == 'd':
      str[i] = 'b'
    elif str[i] == 'p':
      str[i] = 'q'
    else:
      str[i] = 'd'
  
  str = ''.join(str)
  print(f'#{tc} {str}')

# 9940 순열1

for tc in range(1, int(input())+1):
  n = int(input())
  arr = list(map(int, input().split()))
  b = set(arr)
  a = list(b)

  if len(a) == n:
    print(f'#{tc} Yes')
  else:
    print(f'#{tc} No')

# 10761 신뢰
for tc in range(int(input())):
    order = list(input().split())
    N = int(order.pop(0))
 
    # [시간, 위치]
    B = [0, 1]
    O = [0, 1]
     
    # 결과값이 되는 시간
    result = 0
    for i in range(0, 2*N, 2):
        if order[i] == 'B':
            # 이동거리
            d = abs(B[1] - int(order[i+1]))
             
            # 그 위치에 있는 경우 (클릭만 함)
            if d <= result - B[0]:
                B[1] = int(order[i+1])
                result += 1
                B[0] = result
            # 움직인 후 클릭 하는 경우
            else:
                result += d - (result - B[0]) + 1
                B[1] = int(order[i+1])
                B[0] = result
                 
        if order[i] == 'O':
            d = abs(O[1] - int(order[i+1]))

            # 그 위치에 있는 경우 (클릭만 함)
            if d <= result - O[0]:
                O[1] = int(order[i+1])
                result += 1
                O[0] = result
            
            # 움직이고 클릭하는 경우
            else:
                result += d - (result - O[0]) + 1
                O[1] = int(order[i+1])
                O[0] = result
 
    print('#{} {}'.format(tc+1, result))

# 10726 이진수 표현
for tc in range(1, int(input())+1):
  n, m = map(int, input().split())

  count = 0
  tmp = [0]*30
  solve = True
  idx = 0
  while m > 0:
    tmp[idx] = m % 2
    m //= 2
    idx += 1
    if m == 0: break
  
  print(tmp)
  for i in range(n):
    if tmp[i] == 0:
      solve = False
  
  if solve:
    print(f'#{tc} ON')

  else:
    print(f'#{tc} OFF')


# 10570 제곱 팰린드롬 수
import math

def checkPanlindrome(str):
  j = len(str) - 1
  for i in range(int(len(str)/2)+1):
    if str[i] != str[j]:
      return False
    j -= 1
  
  return True


for tc in range(1, int(input())+1):
  a, b = map(int, input().split())
  count = 0
  for i in range(a, b+1):
    tmp = math.sqrt(i)
    if tmp.is_integer():
      if checkPanlindrome(str(i)):
        if checkPanlindrome(str(int(tmp))):
          count += 1
  
  print(f'#{tc} {count}')

# 다른 풀이
for idx in range(1, int(input())+1):
    a,b = map(int,input().split())
    # 정수 판린드롬이 되는 것
    new = [i for i in range(a,b+1) if str(i)==str(i)[::-1]]
    # 제곱근이 정수인 것
    new2 = [j for j in new if j**0.5 == round(j**0.5,1)]
    # 제곱근이 판린드롬 되는 것
    answer = [1 for v in new2 if str(int(v**0.5)) == str(int(v**0.5))[::-1]]
    print(f'#{idx} {sum(answer)}')






