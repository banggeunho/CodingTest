# 코딩테스트 대비 기초 문제 풀이 36일차
# Date : 2022. 02. 24.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 5431. 민석이의 과자 체크하기
for tc in range(1, int(input())+1):
  n, k = map(int, input().split())
  arr = [i for i in range(1, n+1)]
  send = list(map(int, input().split()))
  for i in range(k):
    arr.remove(send[i])

  print(f'#{tc}', end=' ')
  arr.sort()
  for i in arr:
    print(i, end= ' ')

  print()
    

