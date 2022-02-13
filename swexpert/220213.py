# 코딩테스트 대비 기초 문제 풀이 27일차
# Date : 2022. 02. 13.
# 그리디 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 11736. 평범한 숫자

for tc in range(1, int(input())+1):
  n = int(input())
  arr = list(map(int, input().split()))

  count = 0
  for i in range(1, n-1):
    temp = [arr[i-1], arr[i], arr[i+1]]
    if arr[i] == max(temp) or arr[i] == min(temp):
      pass
    else:
      count += 1
  print(f'#{tc} {count}')


# 11588 Calkin-Wilf tree 1
for tc in range(1, int(input())+1):
  arr = list(input())
  a, b = 1, 1
  for i in arr:
    if i == 'L':
      b = a+b
    else:
      a = a+b
  print(f'#{tc} {a} {b}')

# 11445 무한 사전
for tc in range(1, int(input())+1):
  p = list(input().rstrip())
  q = list(input().rstrip())
  solve = False
  for i in range(len(p)):
    if ord(p[i]) < ord(q[i]):
      solve = True
      print(f'#{tc} Y')
      break
  
  if not solve:
    c = 0
    c1 = 0
    for i in p:
      c += ord(i)
    for i in q:
      c1 += ord(i)
    
    if c1 - c > ord('a'):
      print(f'#{tc} Y')
    else:
      print(f'#{tc} N')
  
# 11387 몬스터 사냥
for tc in range(1, int(input())+1):
  d, l, n = map(int, input().split())
  total = d
  for i in range(2, n+1):
    total += d*(1+(i-1)*l/100)

  print(f'#{tc} {int(total)}')

# 11315 오목판정
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [0] * N
    for i in range(N):
        matrix[i] = list(input())
 
    target = ['o'] * 5
    answer = 'NO'
 
    # 가로 세로 확인 (5개 이상인지 체크)
    for i in range(N):
        for j in range(N-4):
            col = [] # 열방향
            row = [] # 행방향
            # 5개 window를 만들어 한칸씩 이동하면서 보겠다.
            for k in range(5):
                row.append(matrix[i][j+k])
                col.append(matrix[j+k][i])
            if row == target or col == target:
                answer = 'YES'
                break
    # 대각선 확인
    for i in range(N-4):
        for j in range(N-4):
            down = []  # 우하향 대각선
            up = []  # 우상향 대각선
            for k in range(5):
                down.append(matrix[i+k][j+k])
                up.append(matrix[j+k][N-1-i-k])
            if down == target or up == target:
                answer = 'YES'
                break
 
    print(f'#{tc} {answer}')
