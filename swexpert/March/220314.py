# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 14.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 두 수의 덧셈 3260
for tc in range(1, int(input())+1):
  a, b = map(int, input().split())
  print(f'#{tc} {a+b}')


# 3233 정삼각형 분할 놀이
for tc in range(1, int(input())+1):
  a, b = map(int, input().split())
  
  cnt = a//b
  cycle, result = 1, 1
  while cycle < cnt:
    result += (cycle*2 + 1)
    cycle += 1

  print(f'#{tc} {result}')


# 3142 영준이와 신비한 뿔의 숲
for tc in range(1, int(input())+1):
  n, m = map(int, input().split())
  print(f'#{tc} {2*m-n} {n-m}')



# 3131 100만 이하의 모든 소수
# 그 수의 제곱근까지만 검색하여 나누어 떨어지면 소수가 아님
import math

def isPrime(n):
  for i in range(2, int(math.sqrt(n)+1)):
    if n % i == 0:
      return False
  return True
  
for i in range(2, 1000001):
  if isPrime(i):
    print(i, end=' ')
  