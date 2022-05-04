# 다시 풀어라 좋은 말로 할때


from collections import deque
n, k, r = map(int, input().split())
load = [[[] for _ in range(n+1)] for _ in range(n+1)]
cow_map = [[False for _ in range(n+1)] for _ in range(n+1)]
cow_list = []

for i in range(r):
    r, c, rr, cc = map(int, input().split())
    load[r][c].append([rr, cc])
    load[rr][cc].append([r, c])

for i in range(k):
    r, c = map(int, input().split())
    cow_list.append([r, c])
    cow_map[r][c] = True

dy = [-1,0,1,0]
dx = [0,1,0,-1]
result = 0
for r, c in cow_list:
    if cow_map[r][c]:
        visited = [[False] *(n+1) for _ in range(n+1)]
        q = deque()
        q.append((r, c))
        cow_map[r][c] = False # 다음 bfs에선 읽지 않음 이 소를
        visited[r][c] = True
        cnt = 0
        k -= 1 #소의 개수를 하나 줄여줌
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
                    if [nx, ny] not in load[x][y]: # 길이 아닌 경우
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        if cow_map[nx][ny]: # 소가 있으면
                            cnt += 1

        result += k-cnt # 자기자신 제외 나머지 소에 대해 갈 수 있는지

print(result)