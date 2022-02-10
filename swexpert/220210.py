# 코딩테스트 대비 기초 문제 풀이 24일차
# Date : 2022. 02. 10.


# SW EXPERT ACADEMY 13547, 팔씨름
test_case = int(input())

for case in range(1, test_case+1):
  result = list(input())
  win_rate = len([i for i in result if i == 'o'])

  if win_rate + (15 - len(result)) >= 8:
      print(f'#{case} YES')
  
  else:
      print(f'#{case} NO')



# SW EXPERT ACADEMY 13229, 일요일
test_case = int(input())

days = { 'MON': 6, 'TUE' : 5, 'WED' : 4, 'THU' : 3, 'FRI': 2, 'SAT' : 1, 'SUN' :  7 }
for case in range(1, test_case+1):
  day = input()
  print(f'#{case} {days[day]}')



# SW EXPERT ACADEMY 13428, 숫자 조작
# 뒤에있는 숫자들을 바꿔서 각각의 경우의 수에서 최댓값, 최솟값을 업데이트 하는 것.

for tc in range(1, int(input()) + 1):
    arr = input()
    N = len(arr)
    print(arr, N)
    max_val = min_val = val = int(arr)
    # 자릿수마다 10의배수로 리스트에 저장
    d = [10 ** i for i in range(N - 1, -1, -1)]
    print(d)
    # 하나씩 뒤에있는 숫자들과 보겠다.
    for i in range(N - 1):
        for j in range(i + 1, N):
          # a = 입력받은 숫자
            a = (val // d[i]) % 10
            b = (val // d[j]) % 10
            print(a, b)
            # 뒤에 값이 0인경우는 넘어간다.
            if i == 0 and b == 0: continue
            # 숫자를 바꿨을때 더 큰 것을 비교해서 min_val max_val 보겠다.
            new_val = val - a * d[i] + a * d[j] - b * d[j] + b * d[i]
            max_val = max(max_val, new_val)
            min_val = min(min_val, new_val)
    print(f'#{tc} {min_val} {max_val}')
