r, c, k = map(int, input().split())
arr = []
visited = [[False] * c for _ in range(r)]
for _ in range(r):
    arr.append((list(input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0
def dfs(x, y, cost):
    global result
    # 이새1끼한테 도달 했을 시 입력한 k랑 같은 cost일 경우 1씩 증가
    if x == 0 and y == c-1:
        if cost == k:
           result += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            # 방문하지 않은 새1끼면서 T가 아닐 경우
            if not visited[nx][ny] and arr[nx][ny] != 'T':
                visited[nx][ny] = True
                dfs(nx, ny, cost+1)
                visited[nx][ny] = False

visited[r-1][0] = True
dfs(r-1, 0, 1)
print(result)