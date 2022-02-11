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



# SW EXPERT ACADEMY 13218, 조별 과제
test_case = int(input())
answers = []
for tc in range(1, test_case+1):
  a, b, c, d = map(int, input().split())
  answers.append(max(min(b,d) - max(a, c),0))
  
for tc in range(1, test_case+1):
  print(f'#{tc} {answers[tc-1]}')


# SW EXPERT ACADEMY 13038, 교환학생

# 풀이 방법 : 처음 수업이 언제 시작 하느냐에 따라서 학교에 머무는 총 일자가 변한다.
# for문을 7번을 돌려(월, 화, 수, 목, 금, 토, 일) 언제 시작하는게 제일 적게 학교에 머무는지 비교한다.
for t in range(int(input())) :
    p = int(input())
    week = list(map(int, input().split()))
    result = 0
 
    for i in range(7) :
        d, n, temp = i, p, 0
         
        while n != 0 :
            temp += 1
            if week[d] == 1 : n -= 1
             
            if d == 6 : d = 0
            else : d += 1
 
        if i == 0 : result = temp
        else : result = min(result, temp)
 
    print(f'#{t+1} {result}')