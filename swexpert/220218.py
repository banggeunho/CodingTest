# 코딩테스트 대비 기초 문제 풀이 32일차
# Date : 2022. 02. 17.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 13240 정사각형 글꼴

# 입력받은 stirng중 가장 길이가 큰 string return한다.
def max_len(str_list):
    tmp = 0
    for v in str_list:
        tmp = max(tmp, len(v))
    return tmp

for tc in range(1, int(input())+1):
  h, w, n = map(int, input().split())
  arr = list(input().split())
  
  ans = max_len(arr)
  # 가장 큰 스트링으로 w를 나눈 몫을 가장 큰 경우의 수로 가정하고
  # 하나씩 포인트를 줄이면서 조건에 맞는 포인트를 찾으면 loop 탈출
  ans = w//ans
  while ans>0:
      hh, ww = ans, 0
      for v in arr:
          # 다음 입력할 단어의 길이 * 포인트 크기
          len_str = len(v)*ans
          # 첫번째 단어는 바로 입력
          if ww==0:
              ww+= len_str
          else:
             # 여기서 ans는 공백이다. 그리고 이전의 ww에 다음단어와 공백을 더한다.
             # 한 줄의 크기가 입력받은 w보다 클 경우 줄바꿈
              if ww+ans+len_str > w:
                 # 줄을 바꿔서 높이에 포인트 크기를 더해준다
                  hh+=ans
                  # 첫번째 단어로 설정해줌
                  ww = len_str
              # 한 줄의 크기가 입력받은 w보다 작을 경우
              else:
                # ww에 더해준다
                  ww += ans + len_str
      
      # 조건에 맞으면 loop 탈출
      if hh <= h and ww <= w:
          break
      # 조건에 맞지 않으면(입력받은 사이즈를 초과할 경우)
      # 한 포인트 줄여서 다시 연산
      ans -= 1

  print(f'#{tc} {ans}')


# 10505 소득 불균형

for tc in range(1, int(input())+1):
  n = int(input())
  arr = list(map(int, input().split()))

  low = [i for i in arr if i <= sum(arr)/len(arr)]

  print(f'#{tc} {len(low)}')

# 10200 구독자 전쟁
for tc in range(1, int(input())+1):
  n, a, b = map(int, input().split())
  max_n = 0
  min_n = 0

  if a == 0 or b == 0:
    max_n = 0
    min_n = 0
  
  else:
    max_n = min(a, b)
    
    if a+b <= n:
      min_n = 0

    else:
      min_n = a+b-n

  print(f'#{tc} {max_n} {min_n}')


# 9700. USB 꽂기의 미스터리

for tc in range(1, int(input())+1):
  p, q = map(float, input().split())

  s1 = (1-p)*q
  s2 = p*(1-q)*q

  if s1 < s2:
    print(f'#{tc} YES')
  else:
    print(f'#{tc} NO')