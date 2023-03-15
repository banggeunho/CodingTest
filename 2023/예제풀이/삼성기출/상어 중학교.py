from collections import deque

# 격자 크기, 색상 개수
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(num, start):

    x, y = start
    q = deque()
    q.append((x, y))
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True

    count = 0
    result = []
    while q:
        cx, cy = q.popleft()
        count += 1
        result.append((cx, cy))

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] != -1 and (arr[nx][ny] == num or arr[nx][ny] == 0):
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return result, count

def gravity():
    for i in range(N-1, -1, -1):
        for j in range(N):
            if arr[i][j] == -1 or arr[i][j] == M + 1:
                continue

            previous = arr[i][j]
            for k in range(1, N):
                nx, ny = i + k*dx[3], j + k*dy[3]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == M+1:
                        arr[nx][ny], arr[i][j] = previous, M+1
                        arr[nx-1][ny] = M+1
                    else:
                        break

# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[n - j - 1][i] = a[i][j]
    return result

total_score = 0

while True:
    # 블록 그룹 탐색
    result_group = []
    max_value = 0
    max_group = []
    for i in range(N):
        for j in range(N):
            # 일반 블록이 하나 이상이어야 되기 때문에
            if 0 < arr[i][j] < M+1:

                result, count = bfs(arr[i][j], (i, j))

                if count >= 2 and max_value < count:
                    max_value = count
                    max_group.clear()

                if count == max_value:
                    max_group.append(result)

    if max_value == 0:
        break

    if len(max_group) > 1:
        max_rainbow_cnt = 0
        max_group2 = []
        for group in max_group:
            count = 0
            for block in group:
                i, j = block
                if arr[i][j] == 0: # 무지개 인 경우
                    count += 1

            if max_rainbow_cnt < count:
                max_rainbow_cnt = count
                max_group2.clear()

            if count == max_rainbow_cnt:
                max_group2.append(group)

        if len(max_group2) > 1:
            temp = []
            for idx, group in enumerate(max_group2):
                group.sort()
                for g1, g2 in group:
                    if arr[g1][g2] != 0:
                        temp.append((g1, g2, idx))
                        break

            temp.sort(reverse=True)
            # 맥스그룹 3 사용
            result_group = max_group2[temp[0][2]]

        else:
            result_group = max_group2[0]
            # 맥스그룹 2 사용

    else:
        #맥스그룹 1 사용
        result_group = max_group[0]

    total_score += (len(result_group) * len(result_group))


    # 블록제거
    for i, j in result_group:
        arr[i][j] = M+1


    # 중력 작용
    gravity()
    # 반시계 방향으로 회전
    arr = rotate_a_matrix_by_90_degree(arr)
    # 중력 작용
    gravity()
    # print(arr)


print(total_score)