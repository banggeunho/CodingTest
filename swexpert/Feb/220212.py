# 코딩테스트 대비 기초 문제 풀이 24일차
# Date : 2022. 02. 10.
# 문제 풀이

# 12004 구구단1
for tc in range(1, int(input())+1):
  n = int(input())
  sol = False
  for i in range(1, 10):
    if not sol:
      for j in range(1, 10):
        if i*j == n:
          print(f'#{tc} Yes')
          sol = True
          break

  if not sol:
    print(f'#{tc} No')

# 12004 구구단2
for tc in range(1, int(input())+1):
  a, b = map(int, input().split())

  if a < 10 and 0 < b < 10:
    print(f'#{tc} {a*b}')

  else:
    print(f'#{tc} {-1}')
    
# 12368 24시간
for tc in range(1, int(input())+1):
  a, b = map(int, input().split())

  if a+b < 24:
    print(f'#{tc} {a+b}')
  elif a+b == 24:
    print(f'#{tc} {0}')
  else:
    print(f'#{tc} {a+b-24}')

# 11856 반반
for tc in range(1, int(input())+1):
  s = list(input())
  c = list()

  for i in s:
    if i not in c:
      c.append(i)
  
  cnt = [0] * len(c)

  for i in range(len(c)):
    for j in s:
      if c[i] == j:
        cnt[i] += 1

  if cnt[0] == 2 and cnt[1] == 2:
    print(f'#{tc} Yes')
  else:
    print(f'#{tc} No')

# 11111 프리섹
for tc in range(1, int(input())+1):
  n, p_d, p_g = map(int, input().split())
  # 퍼센트는 항상 정수임.

  # 오늘 승률이 100이 아닌데 전체 승률이 100인 경우
  if p_d != 100 and p_g == 100:
    print(f'#{tc} Broken')
  
  # 오늘 승률이 0이 아닌데 전체 승률이 0인 경우
  elif p_d != 0 and p_g == 0:
    print(f'#{tc} Broken')
  
  # 승률은 항상 정수
  # 오늘 한 경기랑, 승률을 갖고 나타낼 수 있는지(정수가 되는지)
  else:
    check = False
    for q in range(1, n+1):
      if (q*p_d/100) == (q*p_d//100):
        check = True
        break

    if check:
      print(f'#{tc} Possible')
    
    else:
      print(f'#{tc} Broken')
  

  