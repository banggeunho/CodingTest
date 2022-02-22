# 코딩테스트 대비 기초 문제 풀이 35일차
# Date : 2022. 02. 22.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 6057 그래프의 삼각형

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    edges = list()
    for i in range(M):
        a, b = map(int, input().split())
        edges.append((a,b))
    
    count = 0
    for (a,b) in edges:
      # i, j, k -> (i<j<k)일때 삼각형 그래서 , b+1부터 끝까지 탐색
        for c in range(b+1,N+1):
          # a에 둘 다 연결되어 있는 간선이 존재할 경우 삼각형이라고 간주
            if (a,c) in edges and (b,c) in edges:
                count = count  + 1
    print(f'#{test_case}', count)
