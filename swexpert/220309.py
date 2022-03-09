# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 09.
# 구현 문제 풀이
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------
# 3750 digit sum
answer = []
for tc in range(1, int(input())+1):
  num = list(map(int, input()))

  while len(num) > 1:
    total = sum(num)
    temp = list(map(int, str(total)))
    num = temp

  answer.append(sum(num))
  
for i in range(len(answer)):
  print(f'#{i+1} {answer[i]}')

  
  