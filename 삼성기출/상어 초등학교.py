# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 26.
# 삼성전자 기출 문제
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

# 상어 초등학교 (구현 기출 문제)
# N의 갯수가 최대 20개이므로 N^4이어도 최대 16000개의 경우의 수
# 순차 탐색으로 주어진 조건만 잘 맞춰서 작성하면 무리가 없는 문제

# 각 입력을 받을때마다 순차적으로 전체 map을 확인하면서
# 조건에 맞는 위치에 학생의 번호를 넣어줘야한다.
# 각 조건의 맞는 위치를 찾아 하나의 list(조건이 담긴)로 만들어
# 최종적으로 위치들의 후보들을 갖고 정렬을 수행해 적절한 위치를 뽑아내어 학생으로 업데이트 해준다.

# 자리 배치가 완성되면 처음부터 map을 살펴보면서 점수를 구하면 된다.

n = int(input())
graph = [[0]*n for _ in range(n)]
students={}
for i in range(n**2):
    arr = list(map(int, input().split())) # 0번은 당사자 1번부턴 좋아하는 학생
    students[arr[0]] = arr[1:] # 순서에 관여없이 저장하기 위해 dict로 선언


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 좋아하는 학생 번호를 하나씩 뜯어보면서 적절한 위치를 찾아 update 해준다.
for student, likes in students.items():
    candidates = []
    for x in range(n):
        for y in range(n):
            like, empty = 0, 0
            if graph[x][y] == 0:
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in likes:
                            like += 1
                        elif graph[nx][ny] == 0:
                            empty += 1
                candidates.append([like, empty, n-x, n-y])
    candidates.sort()
    selected = candidates[-1]
    graph[abs(selected[2]-n)][abs(selected[3]-n)] = student

# 점수를 구하는 부분
result = 0
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in students[graph[i][j]]:
                    count += 1

        if count == 1:
            result += 1
        elif count == 2:
            result += 10
        elif count == 3:
            result += 100
        elif count == 4:
            result += 1000

print(result)
    
    
  