# 코딩테스트 대비 코드업 기초 문제 풀이 2일차
# Date : 2022. 01. 20.
# 내가 부족한 문법 & 스킬에 대한 기초 문제 풀이


# codeup 6019
# y, m, d = input().split('.')
# print(d,m,y, sep='-')

# codeup 6026
# a = float(input())
# b = float(input())
# print(a+b)

# codeup 6023
# _,m,_ = input().split(':')
# print(m)

# codeup 6062
# XOR 논리 연산자는 ^으로 사용한다.
# ** 비트단위(bitwise) 연산자는,
# ~(bitwise not), &(bitwise and), |(bitwise or)
# <<(bitwise left shift), >>(bitwise right shift)

# a, b = map(int, input().split())
# print(a^b)

# codeup 6064
# arr = list(map(int, input().split()))
# print(min(arr))

# codeup 6069
# a = input()
# if a == 'A':
#   print('best!!!')
# elif a == 'B':
#   print('good!!')
# elif a == 'C':
#   print('run!')
# elif a == 'D':
#   print('slowly~')
# else:
#   print('what?')

# codeup 6073
# a = int(input())

# while a>0:
#   a -= 1
#   print(a)

# a = int(input())
# b = 1
# result = 0
# while b <= a:
#   if b%2==0: 
#     result+=b
#   b+=1

# print(result)

# while True:
#   a = input()
#   print(a)
#   if a == 'q':
#     break

# a = int(input())
# sum = 0
# num = 0
# for i in range(1, 1000):
#   sum += i
#   num = i
#   if sum >= a:
#     break
# print(num)

# n, m = map(int, input().split())
# for i in range(1, n+1):
#   for j in range(1, m+1):
#     print(i, j)

# a = int(input(),16)
# for i in range(1,16):
#     print('%X*%X=%X' %(a,i,a*i))

# n = int(input())
# for i in range(1, n+1):
#   if i%10==3 or i%10==6 or i%10==9:
#     print('X', end=' ')
#   else:
#     print(i, end=' ')

# r, g, b = map(int, input().split())
# count = 0
# for i in range(r):
#   for j in range(g):
#     for k in range(b):
#       print(i, j, k)
#       count += 1
# print(count)

# h, b, c, s = map(int, input().split())
# print('%.1f MB' % ((h*b*c*s)/8/1024/1024))

h, b, c = map(int, input().split())
# print('%.2f MB' % round(((h*b*c)/8/1024/1024),3))
print('%.2f MB' % ((h*b*c)/8/1024/1024))