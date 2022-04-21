#2075 N번째 큰 수
# 인접 노드에 다른 색깔을 칠할 수 없을때 (같은 색깔을 칠해야만될 때)가 있으면 이분그래프가 아님.
# bfs 이용 인접노드가 색칠 안되어있음 색칠 해주고, 색칠 되어있는데 같은 색깔이면 return
from collections import deque
for tc in range(int(input())):
    v, e = map(int, input().split())
    colors = [0] * (v+1)
    graph = [[] for i in range(v+1)]
    solve = True

    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start, color):
        global solve, colors, graph
        q = deque()
        q.append(start)
        colors[start] = color

        while q:
            # print(q, colors)
            now = q.popleft()
            for adj in graph[now]:
                if colors[adj] == 0:
                    q.append(adj)
                    colors[adj] = colors[now] * (-1)

                elif colors[now] + colors[adj] != 0:
                    solve = False
                    return

    # 모든 정점을 돌면서 확인(연결 & 비연결이라고 안알랴줌)
    for i in range(1, v+1):
        if not solve:
            break
        if colors[i] == 0:
            bfs(i, -1)

    print('YES' if solve else 'NO')