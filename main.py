# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 14.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 3131 100만 이하의 모든 소수
import math

def isPrime(n):
  for i in range(2, int(math.sqrt(n)+1)):
    if n % i == 0:
      return False
  return True
  
for i in range(2, 1000001):
  if isPrime(i):
    print(i, end=' ')
  
    