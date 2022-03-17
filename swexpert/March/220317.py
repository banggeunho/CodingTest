# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 16.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
import itertools
# 2817 부분 수열의 합
for tc in range(1, int(input())+1):
  n, k = map(int, input().split())  
  arr = list(map(int, input().split()))

  result = 0
  for i in range(1, n):
    cases = itertools.combinations(arr, i)
    for case in cases:
      if sum(case) == k:
        result += 1
    
  print(f'#{tc} {result}')

# 2805 농작물 수확하기

for tc in range(1, int(input())+1):
  n = int(input())
  result = 0
  for i in range(n//2, -1, -1):
      s = input()
      for j in range(i, n-i):
        result += int(s[j])
      # 2 1 0 1 2
  for i in range(1, n//2+1):
      s = input()
      for j in range(i, n-i):
        result += int(s[j])   
      
  print(f'#{tc} {result}')
  
      