import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# 도시 초기화
city = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    city[a][b] = min(city[a][b], cost) # 노선이 하나가 아닐 수가 있음.

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                city[i][j] = min(city[i][j], city[i][k] + city[k][j])

# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if city[i][j] == INF:
            print(0, end= ' ')
        else:
            print(city[i][j], end= ' ')

    print()


