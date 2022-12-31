# 백준 9205 맥주마시면서 걸어가기
# 편의점과 목적지를 같은 노드에 넣어서 거리 계산해서 bfs 탐색
# 편의점에 들어가면 맥주는 무조건 20개씩 리필(움직일 수 있는 거리 1000)
# 거리는 맨해튼 계산방식 적용

from collections import deque
for tc in range(int(input())):
    n = int(input())
    solve = False
    s_x, s_y = map(int, input().split())
    node = []
    for _ in range(n):
        x, y = map(int, input().split())
        node.append([x, y])
    d_x, d_y = map(int, input().split())
    node.append([d_x, d_y])
    visited = [False]*(n+1)

    q = deque()
    q.append((s_x, s_y))
    while q:
        x, y = q.popleft()

        # 현재 위치에서 목적지까지 갈 수 있음 리턴
        if abs(x - d_x) + abs(y - d_y) <= 1000:
            print('happy')
            solve = True
            break

        # 어차피 다 편의점이라서 맥주는 항상 20개로 리필
        for i in range(n):
            if not visited[i]:
                nx, ny = node[i][0], node[i][1]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append((nx, ny))
                    visited[i] = 1

    if not solve:
        print('sad')