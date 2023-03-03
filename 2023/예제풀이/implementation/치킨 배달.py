import itertools
n, m = map(int, input().split())
chickens = []
houses = []
idx = 0
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 2:
            chickens.append((idx, i, j))
            idx += 1
        if data[j] == 1:
            houses.append((i, j))

# 치킨집별로 집간의 거리를 저장하기 위함
chicken_dist = [[] for _ in range(len(chickens))]

# 각 치킨집과 집들 사이의 거리를 구한다.
for idx, i, j in chickens:
    for x, y in houses:
        chicken_dist[idx].append(abs(i-x)+abs(j-y))

# 치킨집을 선별하는 case 뽑기
cases = list(itertools.combinations(chicken_dist, m))
result = int(1e9) # 정답을 구하기 위한 변수(최소거리)
for case in cases: # 각 케이스 별로
    tmp_dist = 0
    for i in range(len(case[0])):
        min_dist = int(1e9)
        for j in range(m):
            # 최소 거리 구하기
            if case[j][i] < min_dist:
                min_dist = case[j][i]
        tmp_dist += min_dist # 최소거리 산출

    result = min(result, tmp_dist) # 산출된 치킨 거리 비교
print(result)



