# 코딩테스트 대비 기초 문제 풀이 18일차
# Date : 2022. 02. 05.
# 다이내믹 프로그래밍(DP))

# 다이나믹 프로그래밍(동적 계획법) // 문제풀이

# 효율적인 화폐구성
# N가지 종류의 화폐가 있을 때, 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 해라
# 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화페의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다
# EX) 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 촤소한의 화폐 개수이다.

# n은 화페의 갯수, m은 가치의 합
n, m = map(int, input().split())

# arr은 화폐들 종류를 담는 list
arr = list()
for _ in range(n):
  arr.append(int(input()))

# 화폐의 종류를 작은 것 부터 보기 위해 정렬
arr.sort()

# 화폐의 합이 10000까지이기 때문에, d는 화폐의 합에 따라 최소한의 경우의수를 저장하는 list
d = [10001] * (m+1)

d[0] = 0
# 화폐의 종류를 한개씩 보겠다
for i in range(n):
  # 화폐의 종류별로 m까지 최소한의 경우의 수를 저장하겠다.
  for j in range(arr[i], m+1):
    if d[j - arr[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우
      # 기존의 d에 저장된 값과 d에서 현재 화폐를 뺀것에서 +1 하는 것 중에 작은 경우의 수
      d[j] = min(d[j], d[j-arr[i]] + 1)

if d[m] == 10001:
  print(-1)

else:
  print(d[m])


