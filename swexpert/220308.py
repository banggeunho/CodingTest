# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 08.
# 구현 문제 풀이
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------
# 3499. 퍼펙트 셔플 (swea)
for tc in range(1, int(input())+1):
  n = int(input())
  arr = list(input().split())

  if n % 2 == 0:
    mid = len(arr)//2
  else:
    mid = len(arr)//2+1
  first = arr[:mid]
  second = arr[mid:]
  
  print(f'#{tc}', end = ' ')
  for i in range(len(first)):
    print(first[i], end =' ')
    if i < len(second):
      print(second[i], end = ' ')
  print()
  