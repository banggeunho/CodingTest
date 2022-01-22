# 코딩테스트 대비 코드업 기초 문제 풀이 4일차
# Date : 2022. 01. 22.
# 그리디 알고리즘에 관한 기초 문제 풀이


# 거스름돈 (예제 3-1)
# 거스름돈은 500원, 100원, 50원, 10원이 무한히 존재
# 거슬러줘야할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라.
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

N = int(input())
coin = [500, 100, 50, 10]
count = 0
for i in coin:
  if N == 0:
    break
  count += N // i
  N %= i

print(count)

# 큰 수의 법칙 (예제 3-2)
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
# 2,4,5,4,6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정, 가장 큰 수인 6이 세 번까지만 더해질 수 있음.
# -> 6+6+6+5+6+6+6+5 = 46이 된다. 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first_num = arr[n-1]
second_num = arr[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first_num
    m -= 1

  if m == 0:
    break

  result += second_num
  m -=1

print(result)


# 위 문제의 M의 킉가 100억 이상처럼 커진다면 간단한 수학적 아이디어를 활용
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first_num = arr[n-1]
second_num = arr[n-2]

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += count * first_num
result += (m-count) * second_num

print(result)

# 숫자 카드 게임 (예제 3-3)
n, m = map(int, input().split())

result = 0

for i in range(n):
  arr = list(map(int, input().split()))
  if result < min(arr):
    result = min(arr)
  # reulst = max(result, min(arr))

print(result)

# 숫자 카드 게임 (예제 3-4)
# 1. N에서 1을 뺀다., 2. N을 K로 나눈다.
# N, K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하여라
# 나누는 작업이 제일 횟수가 적으면서 값을 효율적으로 내릴 수 있음.
# 즉, 나누는게 우선시 나누어질 수 없을때 나누어질 수 있는 조건이 될 때까지 1을 뺀다.

n, k = map(int, input().split())
count = 0
while n>1:
  if n % k == 0:
    n /= k
  else:
    n -= 1
  count += 1
print(count)

# N의 수가 엄청 커졌을때 N이 K의 배수가 되는 작업을 한꺼번해 해줘야지 효율적이다.

n, k = map(int, input().split())
count = 0

while True:
  # 1을 뺴는 경우의수를 한꺼번에 계산하여 더한다.
  target = (n//k)*k
  count += n - target
  n = target

  if n < k:
    break
  
  count += 1
  n //= k

# n이 k보다 작을경우 나머지 값을 1씩 뺼경우도 한번에 더해준다
count += (n-1)
print(count)