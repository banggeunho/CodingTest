# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 09.
# 구현 문제 풀이
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------
# 3456 직사각형 길이 찾기
for tc in range(1, int(input())+1):
  arr = list(map(int, input().split()))
  
  for i in arr:
    if arr.count(i) < 2:
      print(f'#{tc} {i}')
      break

    if arr.count(i) > 2:
      print(f'#{tc} {i}')
      break




  
  