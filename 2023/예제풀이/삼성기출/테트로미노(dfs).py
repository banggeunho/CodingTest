n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0
max_pos = max(map(max, arr)) # 지도에서 가장 큰 값

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(pos, step, total):
    global result

    x, y = pos
    # 현재 결과(최댓값)이 현재 남은 스텝에서 최댓값을 다 더한 것 보다 클 때, 리턴
    # => 왜냐면 의미 없기때문
    if result >= total + max_pos*(4-step):
        return

    if step == 4:
        result = max(result, total)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue

        # 'ㅗ' 모양은 기본적인 dfs 못 만듦. 쭉 뻗어 나가는 모양이 아니기 때문, 그래서 자기 자리에서 한 번 더 dfs 수행
        if step == 2:
            visited[nx][ny] = True
            dfs((x, y), step+1, total+arr[nx][ny])
            visited[nx][ny] = False

        # 나머지 모양 (쭉 뻗어 나가는 모양)
        visited[nx][ny] = True
        dfs((nx, ny), step+1, total+arr[nx][ny])
        visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs((i, j), 1, arr[i][j])
        visited[i][j] = False

print(result)
