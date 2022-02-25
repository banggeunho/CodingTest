# 코딩테스트 대비 기초 문제 풀이 36일차
# Date : 2022. 02. 24.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 4579 세상의 모든 팰린드롬 2
for tc in range(1, int(input())+1):
  pattern = input()
  result = "Exist"
  for i in range(0, len(pattern)//2):
    
    if pattern[i] == '*' or pattern[len(pattern)-1-i] == '*':
      break

    if pattern[i] != pattern[len(pattern)-1-i]:
      result = "Not exist"
      break



  # 한글자일때
  if len(pattern) <= 1:
    result = "Exist"
    
  print(f'#{tc} {result}')
    
      
  
