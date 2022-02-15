# 코딩테스트 대비 기초 문제 풀이 29일차
# Date : 2022. 02. 15.
# 그리디 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 만들 수 없는 금액

# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성해라.
# 예 N=5, 3, 2, 1, 1, 9원 동전 -> 8원
# 예 N=3, 3, 5, 7원 동전 -> 1원

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for i in coin:
  if target < i:
    break
  target += i

print(target)

# 볼링공

n, m = map(int, input().split())
ball = list(map(int, input().split()))
count = 0

weight = [0] * 11

for x in ball:
  weight[x] += 1

for i in range(1, m+1):
  n -= weight[i] # 무게가 i인 볼링의 개수를 선택하는 경우 제외
  count += weight[i] * n

print(count)

