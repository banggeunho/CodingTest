# 1. 벽을 세우는 경우의 수
# 2. 벽을 세우고 그래프 탐색으로 바이러스 퍼트리기
# 3. 안전영역 카운트 & 갱신
import copy
from collections import deque
from itertools import combinations

# 동서남북 방향 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 입력
n, m = map(int, input().split())
arr = [] # 지도 입력
virus_idx = [] # 바이러스 위치 입력
safety_idx = [] # 안전구역 위치 입력 (벽 세우는 경우의 수 구할 때 사용)
for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(m):
        if data[j] == 0: # 안전영역 위치
            safety_idx.append((i, j))
        if data[j] == 2: # 바이러스 위치
            virus_idx.append((i, j))

# 벽 세우기
def install_wall(arr, case):
    for (i, j) in case:
        arr[i][j] = 1
    return arr

# 바이러스 퍼트리기 (bfs)
def spread_virus(arr, start):
    x, y = start
    q = deque()
    q.append((x,y))

    while q:
        nx, ny = q.popleft()
        for i in range(4):
            cx, cy = nx + dx[i], ny + dy[i]
            # 지도 범위 내에서 안전 구역일 경우 바이러스 퍼트리기
            if (0 <= cx < n and 0 <= cy < m) and arr[cx][cy] == 0:
                    arr[cx][cy] = 2
                    q.append((cx, cy))

    return arr


# 벽을 세우는 경우의 수 산출
install_cases = list(combinations(safety_idx, 3)) # 벽을 세우는 경우 3으로 고정
result = 0
for case in install_cases:
    # case 별로 사용할 지도와 방문리스트 복사
    tmp_arr = copy.deepcopy(arr)
    # 벽 세우기
    tmp_arr = install_wall(tmp_arr, case)

    # 바이러스 퍼트리기
    for (i, j) in virus_idx:
        tmp_arr = spread_virus(tmp_arr, (i, j))

    # 안전구역 카운트
    count = 0
    for i in range(n):
        count += tmp_arr[i].count(0)

    # 결과 갱신(최댓값)
    result = max(result, count)

print(result)
