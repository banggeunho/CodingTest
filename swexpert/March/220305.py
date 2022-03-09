# 4299 태혁이의 사랑은 타이밍
for tc in range(1, int(input())+1):
  d, h, m = map(int, input().split())

  total = d*24*60 + h*60 + m
  meet = 11*24*60 + 11*60 + 11
  
  if total - meet >=0 :
    print(f'#{tc} {total-meet}')

  else:
    print(f'#{tc} {-1}')



# 4077 영준이의 카드 카운팅
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