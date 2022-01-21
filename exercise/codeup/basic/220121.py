# 코딩테스트 대비 코드업 기초 문제 풀이 3일차
# Date : 2022. 01. 21.
# 내가 부족한 문법 & 스킬에 대한 기초 문제 풀이

# codeup 6086
# a = int(input())
# sum = 0
# i = 1
# while a > sum:
#   sum += i
#   i += 1

# print(sum)

# codeup 6087
# a  = int(input())
# for i in range(1, a+1):
#   if i%3 == 0:
#     pass
#   else:
#     print(i, end=' ')


# codeup 6088
# a, d, n = map(int, input().split())

# print(a+d*(n-1))

# codeup 6089
# a, r, n = map(int, input().split())

# print(a*(r**(n-1)))

# codeup 6090
# a, m, d, n = map(int, input().split())

# for i in range(1, n):
#   a = a*m + d

# print(a)

# codeup 6091
# a, b ,c = map(int, input().split())
# i = 1
# while True:
#   i+=1
#   if i%a == 0 and i%b == 0 and i%c ==0:
#     break
# print(i)
  
# codeup 6092
# n = int(input())
# a = list(map(int, input().split()))
# c = [0 for i in range(23)]

# for i in range(n):
#   c[a[i]-1] += 1

# for i in c:
#   print(i, end=' ')

# codeup 6093
# n = int(input())
# a = list(map(int, input().split()))

# print(min(a))

# codeup 6095
# a = [[0]*19 for i in range(19)]

# n = int(input())
# for _ in range(n):
#   c, d = map(int, input().split())
#   a[c-1][d-1] = 1

# for i in range(19):
#   for j in range(19):
#     print(a[i][j], end=' ')
#   print('')

# codeup 6096
# arr = list()
# for i in range(19):
#   tmp = list(map(int, input().split()))
#   arr.append(tmp)

# n = int(input())
# for _ in range(n):
#     c, d = map(int, input().split())
#     for idx in range(19):
#         arr[c-1][idx] = 1 if arr[c-1][idx] == 0 else 0
#         arr[idx][d-1] = 1 if arr[idx][d-1] == 0 else 0

# for i in range(19):
#   for j in range(19):
#     print(arr[i][j], end=' ')
#   print('')

# code 6097
# # d가 1이면 세로방향, 0이면 가로방향
# # x,y 는 시작하는 좌표(막대의 시작점)
# # l은 막대의 길이
# # 격자판 사이즈 입력, 격자판은 a로 지정
# h, w = map(int, input().split())
# a = [[0]*w for i in range(h)]

# # 막대의 갯수 입력
# n = int(input())

# for _ in range(n):
#   l, d, x, y = map(int, input().split())

#   # 막대의 방향이 가로일경우
#   if d == 0:
#     # x,y 부터 해당 row의 값을 1로 변경
#     for idx in range(y-1, y-1+l):
#       # 막대의 길이가 격자판을 벗어날 경우
#       if idx >= w:
#         break
#       a[x-1][idx] = 1

#     # 막대의 방향이 세로일경우
#   if d == 1:
#     # x,y 부터 해당 column의 값을 1로 변경
#     for idx in range(x-1, x-1+l):
#       # 막대의 길이가 격자판을 벗어날 경우
#       if idx >= h:
#         break
#       a[idx][y-1] = 1

# for i in range(h):
#   for j in range(w):
#     print(a[i][j], end=' ')
#   print('')

# code 6098
arr = list()
for i in range(10):
  tmp = list(map(int, input().split()))
  arr.append(tmp)

cur = 1
# 개미가 밑으로 움직일때
for i in range(1, 10):
  # 개미가 밑으로 움직였을때 먹이면 멈춘다
  if arr[i][cur] == 2:
    arr[i][cur] = 9
    break
  # 개미가 밑에도 벽이면 멈춘다
  if arr[i][cur] == 1:
    break
  for j in range(cur, 10):
    if arr[i][j] == 0:
      arr[i][j] = 9
      cur = j

    if arr[i][j] == 1:
      break
    
    if arr[i][j] == 2:
      arr[i][j] = 9
      cur = j
      break
    if arr[i][cur] == 2:
      break

for i in range(10):
  for j in range(10):
    print(arr[i][j], end=' ')
  print('')
    
