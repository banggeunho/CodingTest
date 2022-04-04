# topology sort인 줄 알았으나, topology로 풀 수 없음....
# 주어진 n의 크기를 보고 플로이드워셜로 문제 풀이
def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        graph[a][b] = 1 # 이겼다
        graph[b][a] = -1 # 졌다
        
        
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if a !=b and graph[a][b] == 0:
                    # a <- k <- b  ==  a <- b (이겼을때)
                    if graph[a][k] == 1 and graph[k][b] == 1:
                        graph[a][b] = 1
                    elif graph[a][k] == -1 and graph[k][b] == -1:
                        graph[a][b] = -1
    

    for i in range(1, n+1):
        # 자기자신만 0일때(즉, 나머지 노드랑 순위관계가 있음)
        if graph[i][1:].count(0) == 1:
            answer += 1
            
    return answer