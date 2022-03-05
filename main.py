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


# 4299 태혁이의 사랑은 타이밍
for tc in range(1, int(input())+1):
  arr = input()
  s = [i for i in range(1, 14)]
  d = [i for i in range(1, 14)]
  h = [i for i in range(1, 14)]
  c = [i for i in range(1, 14)]
  error = False

  for i in range(0, len(arr), 3):
    if arr[i] == 'S':
      if int(arr[i+1:i+3]) in s:
        s.remove(int(arr[i+1:i+3]))
      else:
        print(f'#{tc} ERROR')
        error = True
        break

    elif arr[i] == 'D':
      if int(arr[i+1:i+3]) in d:
        d.remove(int(arr[i+1:i+3]))
      else:
        print(f'#{tc} ERROR')
        error = True
        break

    elif arr[i] == 'H':
      if int(arr[i+1:i+3]) in h:
        h.remove(int(arr[i+1:i+3]))
      else:
        print(f'#{tc} ERROR')
        error = True
        break

    else:
      if int(arr[i+1:i+3]) in c:
        c.remove(int(arr[i+1:i+3]))
      else:
        print(f'#{tc} ERROR')
        error = True
        break


  if not error:
    print(f'#{tc} {len(s)} {len(d)} {len(h)} {len(c)}')
  

