# 코딩테스트 대비 기초 문제 풀이 40일차
# Date : 2022. 03. 03.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14502
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 4522. 세상의 모든 팰린드롬
for tc in range(1, int(input())+1):
  str = list(input())
  
  for i in range(0, len(str)//2):
    if str[i] == '?' or str[len(str)-1-i] == '?':
      str[i], str[len(str)-1-i] = '?', '?'
  
  if str == str[::-1]:
    print(f'#{tc} Exist')

  else:
    print(f'#{tc} Not exist')

  
# 4406 모음이 보이지 않는 사람
for tc in range(1, int(input())+1):
  str = list(input())

  mo = ['a','e','i','o','u']
  print(f'#{tc}', end=' ')
  for alpha in str:
    if alpha not in mo:
      print(alpha, end='')
  print()

# 4371 항구에 들어오는 배

for tc in range(1, int(input())+1):
  n = int(input())
  arr = [int(input()) for _ in range(n)]
       
  # 첫번째 배는 무조건 1이 들어온다는 가정하에 풀이
  for i in arr[1:]:
    # 두번째-첫번째=주기,로 지정 후에 마지막까지 검사
    # 세번째-첫번째 주기, 네번째-첫번째 주기.......
    # array가 다 지워질때까지............
    for j in range(2*i-1, arr[-1]+1, i-1):
      if j in arr:
        arr.remove(j)

  print(f'#{tc} {arr[1:]}')
  
    

  
  