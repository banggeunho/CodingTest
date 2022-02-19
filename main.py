# 코딩테스트 대비 기초 문제 풀이 32일차
# Date : 2022. 02. 17.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 5688 세제곱근을 찾아라
for tc in range(1, int(input())+1):
  n = int(input())
  # n-1의 세제곱근을 구하여 그것보다 큰것부터 보면 되겠다 인수형으로 바꿔서 ㅇㅈ?
  solve = False

  if round(n**(1/3), 1) - int(round(n**(1/3), 1)) == 0:
    x = int(round(n**(1/3), 1))
    if pow(x, 3) == n:
      solve = True

  if not solve:
    print(f'#{tc} {-1}')
  
  else:
    print(f'#{tc} {int(x)}')



# 7675 통역사 성경이

for tc in range(1, int(input())+1):
  n = int(input())
  arr = list(input().split())
  count = [0] * n
  idx = 0

  for i in arr:
    # 첫글자 대문자
    # print(i)
    if len(i) == 1 and 'A'<= i[0] <= 'Z':
      count[idx] += 1
      continue

    if 'A' <= i[0] <= 'Z':
      for j in range (1, len(i)):
        # 마지막 전까지 대문자가 등장 경우 탈출
        if len(i) - j > 1 and not('a' <= i[j] <= 'z'):
          # print('소문자 아님')
          break

        # 마지막까지 소문자일 경우 count 증가
        if len(i) - j == 1 and 'a' <= i[j] <= 'z':
          count[idx] += 1
          # print('이름 발견')
          break

        # 마지막이 구두점이면 count 추가 문장바꿈
        if len(i) - j == 1 and (i[j] =='.' or i[j] =='!' or i[j] == '?'):
          count[idx] += 1
          # print('이름 발견')
        

    # 마지막이 구두점이면 문장 바꿈
    if i[-1] =='.' or i[-1] =='!' or i[-1] == '?':
        idx += 1
        # print('문장 바꿈')



  print(f'#{tc}', end=' ')
  for i in count:
    print(i, end=' ')
  print()      
