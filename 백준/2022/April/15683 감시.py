'''
입력 부분 : 카메라의 위치, type 저장
카메라의 방향 : dx, dy의 변수에 맞게 모든 경우 저장(방향이 많지 않기 때문에 전체 탐색 가능)
fill 함수 : 각 감시 방향에 따라 지도를 채우는 함수
dfs 함수 : 각각의 경우에 따라 감시방향이 채워지는 지도를 만들어가는 함수
dfs 함수에서 각각의 카메라의 정보를 불러와 감시 방향으로 채워질 수 있는 경우만큼 dfs 가지를 쳐준다.
그 후 각각의 fill함수도 수행 -> 모든 cctv에 대해 모든 경우의 수를 탐색을 다 했을 경우
각각의 채워진 지도에 0의 갯수를 세서 최솟값을 찾으면 끝.
'''
n, m = map(int, input().split())
arr = []
cctv = []

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j]) # 카메라 위치 저장

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [
    [],
    [[0], [1], [2], [3]], # 4가지
    [[0, 2], [1, 3]], # 2가지
    [[0, 1], [1, 2], [2, 3], [0, 3]], # 4가지
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], # 4가지
    [[0, 1, 2, 3]] #1가지
]

def fill(arr, mm, x, y): # 감시지역 채우기
    for i in mm: # 해당 방향에 맞게 감시지역 채우기~~~~
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0<= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 7

                if arr[nx][ny] == 6: #벽일 경우
                    break
            else: # 지도 범위를 벗어난 경우
                break

import copy
def dfs(depth, arr):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(n): # 0인 구역 세기
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return

    temp = copy.deepcopy(arr)
    cctv_type, x, y = cctv[depth]
    for i in mode[cctv_type]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr) # temp값 초기화

min_value = int(1e9)
dfs(0, arr)
print(min_value)