# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 14.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 공유기 설치
# 인덱스로 바이너리 서치를 하는게 아닌 가능한 이격 거리를 줄이면서 바이너리 서치 하는 것이 포인트
n, c = map(int, input().split())
house, result = [], []
for _ in range(n):
  house.append(int(input()))
house.sort()

value = house[0]
start = 1 # 가능한 최소 거리(min gap)
end = house[-1] - house[0] # 가능한 최대 거리 (max gap)

while start <= end:
  mid = (start+end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리를(gap) 의미
  value = house[0]
  count = 1

  # 현재 mid값을 이용해 공유기 설치
  for i in range(1, n): #앞에서부터 순서대로 설치
    if house[i] >= value + mid:
      value = house[i]
      count += 1

  if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
    start = mid + 1
    result = mid # 최적의 결과를 저장

  else: # C개 이상의 공유기를 설치할 수 없는 경우
    end = mid - 1

print(result)




  