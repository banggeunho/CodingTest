import heapq
distance = []

# 우선순위 큐를 이용한 dijkstra 알고리즘
def dijkstra(start, graph):
    global distance
    q = []
    heapq.heappush(q, (0, start)) # 최단거리, 노드 번호
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: # 이미 건드렸다면 넘어가
            continue
            
        for i in graph[now]: # 연결된 주변 노드 탐색
            cost = dist + i[1]
            if cost < distance[i[0]]: # 거리가 작은게 있다면 update후, 큐에 넣어줘
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                

def solution(n, edge):
    global distance
    answer = 0
    graph = [[] for i in range(n+1)]
    INF = int(1e9)
    distance = [INF] * (n+1) # 최단거리 저장 list
    # 그래프 list에 각 엣지에 대한 정보 (거리는 1로 설정)
    for i in edge:
        graph[i[0]].append((i[1], 1))
        graph[i[1]].append((i[0], 1))
    
    # 다익스트라
    dijkstra(1, graph)
    max_dis = max(distance[1:])

    for i in range(1, n+1):
        if max_dis == distance[i]:
            answer += 1
    return answer