# 상어는 고유한 번호를 가지고 있음
# 1의 번호를 가진 어른 상어는 나머지 모두를 쫒아낼 수 있음

# 냄새를 자기 자신 자리의 뿌린다. (arr에는 상어의 번호와 냄새가 남은 시간을 저장)
# - 냄새는 k번 이동하고 나면 사라진다.
# 상하좌우 인접칸 중 하나로 이동
# 이동방향 결정
# 1. 아무 냄새가 없는 칸
# 2. 그런 칸이 없으면 자신의 냄새가 있느 칸의 방향으롲 잡는다
#    1) 여러개가 있으면 특정한 우선순위를 따른다(입력으로 받음)
#    각 방향을 가지고 있을떄 마다 다른 우선순위를 갖고 있음.
# 3. 이동하고 나면 이동한 방향이 상어가 보고 있는 방향이 된다.
# 이동했을때 1번 상어부터 이동하니 그 다음 상어도 같은 위치에 올 경우 사라진다.
# 1번 상어만 남기까지 걸리는 시간을 출력, 1000초가 넘어도 다른 상어가 격자에 남아있으면 -1을 출력
# 1, 2, 3, 4 위 아 왼 오
# 입력 받을때, 위ㅡ아ㅡ왼-오


n, m, k = map(int, input().split()) # 크기, 상어, 냄새지속시간
arr = [[] for i in range(n)] # 지도 배열
d_p = [[] for i in range(m)] # 각 상어새끼들의 방향에 따른 우선순위 저장
dead_shark = [] # 죽은 새1끼들 저장
# 입력받는 부분 (상어 번호, 냄새 번호, 냄새 지속 시간)으로 넣어줌
for i in range(n):
    data = list(map(int, input().split()))
    for j in data:
        arr[i].append([j, 0, 0])  # 상어 번호, 냄새 번호, 냄새지속시간

# 상어의 현재 방향 입력받는다 ( 현재 방향을 계속 업데이트 해준다.
s_d = list(map(int, input().split()))

for i in range(m):
    for j in range(4):
        d_p[i].append(list(map(int, input().split())))

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while len(dead_shark) < m-1: # 살아남은 새1끼가 한마리일 때까지 돌려
    time += 1

    if time > 1000:  # 종료 조건
        time = -1
        break

    # 지속시간 하나씩 줄이기
    for i in range(n):
        for j in range(n):
            if arr[i][j][2] != 0: # 냄새 지속시간이 0이 아닌경우
                arr[i][j][2] -= 1 # 지속시간 감소
                if arr[i][j][2] == 0: # 남아있는 지속시간이 없으면
                    arr[i][j][1] = 0 # 냄새 없애기


    # 냄새 뿌리기
    for i in range(n):
        for j in range(n):
            if arr[i][j][0] != 0: # 상어가 위치한 곳 찾기
                arr[i][j][1] = arr[i][j][0] # 상어의 번호에 맞게 냄새를 뿌린다
                arr[i][j][2] = k # 냄새 지속시간 부여


    # 이동하기
    visited = [False]*(m+1)
    for i in range(n):
        for j in range(n):
            isMove = False
            if arr[i][j][0] > 0 and not visited[arr[i][j][0]] and arr[i][j][0] not in dead_shark: # 상어가 있는 경우, 죽지 않은 경우, 이동했던 상어가 아닐 경우
                for l in d_p[arr[i][j][0]-1][s_d[arr[i][j][0]-1]-1]: # 자신의 방향에 따른 우선순위 보면서 빈 칸으로 이동하겠다.
                    nx = i + dx[l-1]
                    ny = j + dy[l-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny][1] == 0: # 아무 냄새가 없는 칸
                            visited[arr[i][j][0]] = True
                            if arr[nx][ny][0] != 0: # 상어가 있을때
                                if arr[nx][ny][0] > arr[i][j][0]: # 나보다 번호가 큰 새끼일 경우
                                    dead_shark.append(arr[nx][ny][0]) # 상어 죽이기
                                    arr[nx][ny][0] = arr[i][j][0] # 상어 움직이기
                                    s_d[arr[i][j][0] - 1] = l  # 이동한 방향으로 상어 방향 바꿔주기
                                    arr[i][j][0] = 0  # 이동 전 빈칸
                                else: # 나보다 작은 새끼일 경우
                                    dead_shark.append(arr[i][j][0])
                                    arr[i][j][0] = 0

                            elif arr[nx][ny][0] == 0: # 상어가 없는 경우
                                arr[nx][ny][0] = arr[i][j][0]
                                s_d[arr[i][j][0] - 1] = l  # 이동한 방향으로 상어 방향 바꿔주기
                                arr[i][j][0] = 0

                            isMove = True
                            break

                # 냄새가 비어있는 곳이 없었을 경우
                if not isMove:
                    for l in d_p[arr[i][j][0]-1][s_d[arr[i][j][0]-1]-1]:
                        nx = i + dx[l - 1]
                        ny = j + dy[l - 1]
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny][1] == arr[i][j][0]:  # 자기 냄새
                                arr[nx][ny][0] = arr[i][j][0]
                                s_d[arr[i][j][0] - 1] = l # 이동한 방향으로 상어 방향 바꿔주기
                                visited[arr[i][j][0]] = True
                                arr[i][j][0] = 0  # 이동한 곳은 빈칸
                                break

# print(dead_shark)
print(time)