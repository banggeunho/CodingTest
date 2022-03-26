# BFS 문제
# BFS를 이용하여 상어가 먹을 수 있는 물고기들의 리스트들을 뽑아낸다.
# 리스트의 갯수에 따라 문제에서 주어진 조건에 맞게 문제를 수행하면 된다.
# 물고기를 많이 먹을 경우, 상어의 크기가 커지는 특성을 고려해 무한 루프를 cover 해줘야 한다.
# 먹을 수 있는 물고기가 없을때 까지 loop를 살려주면 된다.


from collections import deque

n = int(input())
graph = []
s_size = 2
s_x, s_y = 0, 0
result = 0
eated = 0  # 물고기 몇마리 먹었는지
# 공간 입력 받기
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if graph[i][j] == 9:
            s_x, s_y = i, j

# 먹을 수 있는 물고기가 2마리 이상일때
# 주변으로 이동했을떄 타겟팅한 물고기와의 위치를 연산해서 최솟값을 나타내는 부분을 찾아야함

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    temp = 0  # 몇칸 이동했는지
    visited = [[False] * n for _ in range(n)]  # 방문했는지
    mulgogi = []
    q = deque()
    q.append((s_x, s_y, temp))
    visited[s_x][s_y] = True # 상어 출발 위치 방문 처리
    graph[s_x][s_y] = 0 # 상어 위치 0으로 변경

    while q:
        x, y, temp = q.popleft()  # 상어의 현재 위치 (위치, 이동횟수)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= s_size:  # 물고기의 크기가 상어랑 사이즈가 동일하거나 작으면 이동가능
                    q.append((nx, ny, temp + 1))
                    visited[nx][ny] = True

                    if 0 < graph[nx][ny] < s_size : # 물고기인 경우
                        mulgogi.append((temp+1, nx, ny)) # 이동한 값으로 정렬하기 위해 보기와 같은 순서로 저장

    if len(mulgogi) == 0: # 먹을 수 있는 물고기가 없음
        break

    else: # 먹을 수 있는 물고기 1마리
        mulgogi.sort() # 1마리 이상일 경우 대비해서 sort
        dist, x, y = mulgogi[0]
        result += dist # 결과 업데이트
        graph[x][y] = 9 # 지도 업데이트
        s_x, s_y = x, y # 상어 위치 업데이트
        eated += 1
        if eated == s_size: # 물고기 먹은 횟수가 상어의 사이즈랑 동일할 경우
            s_size += 1
            eated = 0

print(result)
