# https://www.codetree.ai/training-field/frequent-problems/problems/destroy-the-turret/description?page=1&pageSize=20
# 지도 정보
# N X M 격자가 있고, 모든 위치에는 포탑이 존재한다. (포탑의 개수는 NM 개))
# 최초에 공격력이 0인 포탑, 즉 부서진 포탑이 존재 가능
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
tower = [[0] * M for _ in range(N)]
broken_cnt = 0
for i in range(N):
    for j in range(M):
        tower[i][j] = (0, board[i][j])  # 공격 시점, 공격력
        if board[i][j] == 0:
            broken_cnt += 1

# 턴 정보 (K번의 턴 반복 합니다.)
# 하나의 턴은 다음의 4가지 액션을 순서대로 수행
# 1. 공격자 선정
# 0이 아닌 포탑 중 가장 숫자가 낮은 포탑이 공격자로 선정
# 공격력이 가장 낮은 포탑이 공격자로 선정, 가장 최근에 공격한 포탑이 가장 약한 포탑. (모든 포탑은 시점0에 모두 공격한 경험이 있다고 가정)
# 1.공격력이 가장 낮은 포탑
time = 1
while time <= K:
    # print(time, "============")
    attack_tower = ()
    min_power = 5001
    for i in range(N):
        for j in range(M):
            if tower[i][j][1] != 0:
                min_power = min(min_power, tower[i][j][1])

    min_power_list = [(tower[i][j][0], i + j, j) for i in range(N) for j in range(M) if min_power == tower[i][j][1]]
    if len(min_power_list) == 1:
        attack_tower = (min_power_list[0][1] - min_power_list[0][2], min_power_list[0][2])
    # 2.가장 최근에 공격한 포탑 (시점0에는 모두 공격한 경험이 있다고 가정)
    # 3.각 포탑 위치의 행과 열의 합이 가장 큰 포탑
    # 4.각 포탑 위치의 열 값이 가장 큰 포탑
    else:
        min_power_list.sort(key=lambda x: [-x[0], -x[1], -x[2]])
        attack_tower = (min_power_list[0][1] - min_power_list[0][2], min_power_list[0][2])

    # 5. 공격자 최근 공격정보 업데이트
    # -> N + M 만큼의 공격력이 증가함
    x, y = attack_tower
    tower[x][y] = (time, tower[x][y][1] + N + M)

    # 2. 공격
    # 1번에서 선정된 공격자는 자신을 제외한, 가장 강한 포탑을 공격
    # 1. 공격력이 가장 높은 포탑
    attacked_tower = ()
    max_power = 0
    for i in range(N):
        for j in range(M):
            if tower[i][j][1] > 0 and (i, j) != attack_tower:
                max_power = max(max_power, tower[i][j][1])

    max_power_list = [(tower[i][j][0], i + j, j) for i in range(N) for j in range(M) if max_power == tower[i][j][1]]
    if len(max_power_list) == 1:
        attacked_tower = (max_power_list[0][1] - max_power_list[0][2], max_power_list[0][2])
    # 2. 공격한지 가장 오래된 포탑 (모든 포탑은 시점 0에 모두 공격한 경험이 있음)
    # 3. 행과 열의 합이 가장 작은 포탑
    # 4. 열 값이 가장 작은 포탑
    else:
        max_power_list.sort()
        attacked_tower = (max_power_list[0][1] - max_power_list[0][2], max_power_list[0][2])

    x, y = attacked_tower
    # 2-1. 레이저 공격
    # 상하좌우의 4개 방향으로 움직일 수 있음
    # 1. 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택
    dx4 = [0, 1, 0, -1]
    dy4 = [1, 0, -1, 0]
    visited = [[False] * M for _ in range(N)]
    a_x, a_y = attack_tower
    visited[a_x][a_y] = True
    path_result = []

    # 레이저 공격은 공격자 위치에서 공격 대상 포탑까지의 최단 경로로 공격합니다.
    from collections import deque

    q = deque()
    q.append((a_x, a_y, []))

    while q:
        cx, cy, path = q.popleft()
        if (cx, cy) == attacked_tower:
            path_result = path

        for i in range(4):
            # 부서진 포탑이 있는 위치는 지날 수 없음
            # 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나옵니다 (보드는 연결되어있다 가정)
            nx = (cx + dx4[i]) % N
            ny = (cy + dy4[i]) % M

            if tower[nx][ny][1] > 0 and not visited[nx][ny]:
                q.append((nx, ny, path + [(nx, ny)]))
                visited[nx][ny] = True

    ad_x, ad_y = attacked_tower
    fighted_tower = [attack_tower, attacked_tower]
    # print('공격자', tower[a_x][a_y], a_x, a_y, '공격대상', tower[ad_x][ad_y], ad_x, ad_y)
    # print(path_result)

    if path_result:
        # print("레이저 공격 시도", attack_tower, ' -> ', attacked_tower)
        # 공격 대상에는 공격자의 공격력 만큼의 피해를 입힙니다 (공격력이 줄어들어야 함)
        tower[ad_x][ad_y] = (tower[ad_x][ad_y][0], tower[ad_x][ad_y][1] - tower[a_x][a_y][1])

        # 레이저 경로에 있는 포탑도 공격을 받습니다. (공격자의 절반 만큼 공격을 받습니다. 2로 나눈 몫)
        for x, y in path_result:  # 공격대상 제외
            if (x, y) == attacked_tower:
                continue
            tower[x][y] = (tower[x][y][0], tower[x][y][1] - int(tower[a_x][a_y][1] / 2))
            fighted_tower.append((x, y))

    # 최단 경로가 없다면 포탄 공격을 시도합니다.
    # 2-2. 포탄 공격
    else:
        # print("포탄 공격 시도", attack_tower, ' -> ', attacked_tower)
        dx8 = [0, 1, 0, -1, 1, 1, -1, -1]
        dy8 = [1, 0, -1, 0, -1, 1, -1, 1]
        # 공격대상은 공격자의 공경력 만큼 피해를 받습니다.
        # 공격 대상에는 공격자의 공격력 만큼의 피해를 입힙니다 (공격력이 줄어들어야 함)
        tower[ad_x][ad_y] = (tower[ad_x][ad_y][0], tower[ad_x][ad_y][1] - tower[a_x][a_y][1])
        # 공격대상 주위의 8개 방향에 있는 포탑도 절반만큼 피해를 받습니다. (2로 나눈 몫)

        for i in range(8):
            # 만약 가장자리에 포탄이 떨어졌다면, 반대편 격자에 영향을 미치게 됩니다.
            nx = (ad_x + dx8[i]) % N
            ny = (ad_y + dy8[i]) % M

            # 공격자는 해당 공격에 영향을 받지 않습니다.
            if tower[nx][ny][1] > 0 and (nx, ny) != attack_tower:
                tower[nx][ny] = (tower[nx][ny][0], tower[nx][ny][1] - int(tower[a_x][a_y][1] / 2))
                fighted_tower.append((nx, ny))

    # 3. 공격을 받아 공격력이 0 이하가 된 포탑은 부서집니다.
    # # print('영향받은 포탑', fighted_tower)
    for x, y in fighted_tower:
        if tower[x][y][1] <= 0:
            tower[x][y] = (tower[x][y][0], 0)
            broken_cnt += 1

    # 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지됩니다.
    if broken_cnt == N * M - 1:
        break

    # # print(' ==== 공격 직후 =====')
    # for i in range(N):
    #     # print(*tower[i])

    # 4.포탑 정비
    # 공격이 끝났으면, 부서지지 않은 포탑 중 공격과 무관했던 포탑은 공력이 1씩 올라갑니다.
    # 공격자도 아니고, 공격 대상도 아니고, 공격에 피해를 입은 포탑도 아닙니다.
    for i in range(N):
        for j in range(M):
            if tower[i][j][1] > 0 and (i, j) not in fighted_tower:
                tower[i][j] = (tower[i][j][0], tower[i][j][1] + 1)

    # print(' ==== 정비 직후 =====')
    # for i in range(N):
    # print(*tower[i])

    time += 1

flattened_list = [item for sublist in tower for item in sublist]
print(max(flattened_list, key=lambda x: x[1])[1])