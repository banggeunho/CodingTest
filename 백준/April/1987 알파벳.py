# dfs 문제
n, m = map(int, input().split())
arr = []
visited = set()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(n):
    arr.append(list(input()))

result = 0
def dfs(x, y, cost):
    global result
    result = max(result, cost)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] not in visited:
                visited.add(arr[nx][ny])
                dfs(nx, ny, cost+1)
                visited.remove(arr[nx][ny])

visited.add(arr[0][0])
dfs(0, 0, 1)
print(result)