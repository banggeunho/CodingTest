# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 04.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14888
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 3975 승률 비교하기
answer = []
for tc in range(1, int(input())+1):
  a, b, c, d = map(int, input().split())
  if (a/b) > (c/d):
    answer.append('ALICE')
  elif (a/b) < (c/d):
    answer.append('BOB')
  else:
    answer.append('DRAW')

for tc, i in enumerate(answer):
  print(f'#{tc+1} {i}')