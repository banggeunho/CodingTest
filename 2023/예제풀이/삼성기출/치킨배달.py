def calculator():
    result = 0
    for hx, hy in house:
        dist = float('inf')

        for idx, (cx, cy) in selected_chicken:
            dist = min(dist, abs(hx - cx) + abs(hy - cy))

        result += dist
    res.append(result)

def select_chicken(count):
    if count == m:
        print(selected_chicken)
        calculator() # 치킨 거리 계산
        return

    for idx, (x, y) in enumerate(chicken):
        if not visited[x][y]:
            if selected_chicken:
                if idx < selected_chicken[-1][0]: # 중복 경우의 수 생기지 않게 방지
                    continue

            # 백트랙킹 기법 사용~
            visited[x][y] = True
            selected_chicken.append((idx, (x, y)))
            select_chicken(count + 1)
            visited[x][y] = False
            selected_chicken.pop()

n, m = map(int, input().split())
visited = [[False] * n for _ in range(n)]
selected_chicken = []
res = []

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

select_chicken(0)
print(min(res))