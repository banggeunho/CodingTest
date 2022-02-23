# 코딩테스트 대비 기초 문제 풀이 36일차
# Date : 2022. 02. 24.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 5986. 새샘이와 세 소수

def isPrimeNum(n):
  count = 0
  idx = 0
  for i in range(2, n+1):
    if n%i == 0:
      count += 1
      idx = i
      break

  if idx == n and count == 1:
    return True

  return False
    
  
for tc in range(1, int(input())+1):
  n = int(input())
  count = 0
  primeNum = [i for i in range(2, 1000) if isPrimeNum(i)]
  stop = False
  # print(primeNum)
  for i in range(0, len(primeNum)):
    for j in range(i, len(primeNum)):
      if primeNum[i]+primeNum[j] > n:
        stop = True
        break
      # print(primeNum[i], primeNum[j], n-(primeNum[i]+primeNum[j]))
        
      if n-(primeNum[i]+primeNum[j]) in primeNum and (n-(primeNum[i]+primeNum[j]) >= primeNum[j] >= primeNum[i]):
        count += 1
        # print('OK')

      elif primeNum[j] > n-(primeNum[i]+primeNum[j]):
        break
      
    if stop:
      break
      
  print(f'#{tc} {count}')
