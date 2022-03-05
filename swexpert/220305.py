# 4299 태혁이의 사랑은 타이밍
for tc in range(1, int(input())+1):
  d, h, m = map(int, input().split())

  total = d*24*60 + h*60 + m
  meet = 11*24*60 + 11*60 + 11
  
  if total - meet >=0 :
    print(f'#{tc} {total-meet}')

  else:
    print(f'#{tc} {-1}')