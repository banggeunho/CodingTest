# 코딩테스트 대비 기초 문제 풀이 40일차
# Date : 2022. 02. 28.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14502
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

for tc in range(1, int(input())+1):
  str = input()
  h = int(input())
  idx = list(map(int, input().split()))
  idx.sort()

  def counting(arr, a):
    count = 0
    for i in arr:
      if i == a:
        count+=1
    return count

  a = set(idx)
  b = list(a)

  temp = ""
  if 0 in b:
    temp = '-'*counting(idx, 0)
    
  for i in range(len(str)):
    temp += str[i] + ('-'*counting(idx, i+1))
      
  print(f'#{tc} {temp}')
  # print(''.join(str))
  
    

  
  