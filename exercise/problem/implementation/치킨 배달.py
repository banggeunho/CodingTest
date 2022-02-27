# 코딩테스트 대비 기초 문제 풀이 36일차
# Date : 2022. 02. 27.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 치킨 배달
# 백준 15686
import itertools

n, m = map(int, input().split())
mat = []
for i in range(n):
  mat.append(list(map(int, input().split())))

# 치킨집, 집 주소 저장
chicken = []
house = []
for i in range(n):
  for j in range(n):
    # 치킨집
    if mat[i][j] == 1:
      house.append([i, j])
    # 집
    elif mat[i][j] == 2:
      chicken.append([i, j])
    else:
      continue


answer = int(1e9)
for j in itertools.combinations(chicken, m):
  chicken_dis = 0
  for k in house:
    min_chicken = int(1e9)
    for l in j:
      min_chicken = min(min_chicken, abs(k[0]-l[0]) + abs(k[1]-l[1]))
    chicken_dis += min_chicken
  answer = min(answer, chicken_dis)
  
print(answer)

# 치킨 배달
import itertools

n, m = map(int, input().split())
# 치킨집, 집 주소 저장
chicken = []
house = []
for r in range(n):
  mat = list(map(int, input().split()))
  for c in range(n):
    # 치킨집
    if mat[c] == 1:
      house.append((r, c))
    # 집
    elif mat[c] == 2:
      chicken.append((r, c))


candidates = itertools.combinations(chicken, m)

def getsum(candidate):
  result = 0
  for hx, hy in house:
    temp = 1e9
    for cx, cy in candidate:
      temp = min(temp, abs(hx-cx) + abs(hy-cy))
    result += temp
  return result
  
answer = 1e9
for candidate in candidates:
  answer = min(answer, getsum(candidate))
  
print(answer)