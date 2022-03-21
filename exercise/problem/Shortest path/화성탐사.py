# 화성 탐사(ACM-ICPC) (2차원 배열 활용 다익스트라)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

for tc in range(1, int(input())+1):
    n= int(input())
    graph = []
    distance = [[INF]*n for _ in range(n)]

    # 간선의 정보를 받아와줍니다
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정
    # queue에는 (에너지, x, y) 값이 들어갑니다.
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        energy, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있으면 무시
        if distance[x][y] < energy:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
             # 큐에서 꺼낸 노드의 상하좌우 확인
                cost = energy + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])
