# 코딩테스트 대비 기초 문제 풀이 23일차
# Date : 2022. 02. 09.
# SW EXPERT ACADEMY 문제 풀이 (9658 유효숫자 표기)

import math
test_case = int(input())

def len_num(n):
  len = 0
  while n >= 10:
    n //= 10
    len += 1
    # print(n, 'len=', len)
  return len


for i in range(test_case):
  n = int(input())
  exp = len_num(n)
  result = n / math.pow(10, exp)
  result = round(result, 1)

  # 반올림 했을때 정수부가 두 자릿수가 되면은 처리해준다.
  if result >= 10:
    result //= 10
    exp += 1

  print(f'#{i+1} {result}*10^{exp}')