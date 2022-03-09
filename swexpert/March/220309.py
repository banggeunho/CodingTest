# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 09.
# 구현 문제 풀이
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------
# 3750 digit sum
answer = []
for tc in range(1, int(input())+1):
  num = list(map(int, input()))

  while len(num) > 1:
    total = sum(num)
    temp = list(map(int, str(total)))
    num = temp

  answer.append(sum(num))
  
for i in range(len(answer)):
  print(f'#{i+1} {answer[i]}')


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

  
# 3431 준환이의 운동 관리
for test_case in range(1, int(input()) + 1):
  a, b, c = map(int, input().split())
  if c < a:
    print(f'#{test_case} {a-c}')
  elif b < c:
    print(f'#{test_case} {-1}')
  elif a <= c <= b:
    print(f'#{test_case} {0}')


# 3408 세가지의 합
for tc in range(1, int(input())+1):
  n = int(input())
  print(f'#{tc} {n*(n+1)//2} {n*n} {n*(n+1)}')