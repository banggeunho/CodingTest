from collections import deque

n, k = map(int, input().split())
arr = []
virus_idx = [[] for i in range(k+1)] # 번호 별 바이러스 위치 저장
for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(n):
        if data[j] != 0:
            virus_idx[data[j]].append((i, j))

s, x, y = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 바이러스 증식(지도, 바이러스 번호)
def spread_virus(arr, k):
    temp = [[] for _ in range(k+1)] # 새로 증식된 바이러스를 담을 리스트
    q = deque([k])
    while q:
        now = q.popleft()
        for cx, cy in virus_idx[now]: # 해당 번호의 바이러스 위치 확인
            for i in range(4): # 방향별 확인
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                    arr[nx][ny] = now # 지도 업데이트
                    temp[k].append((nx, ny)) # 증식된 자리 추가
    return arr, temp

for _ in range(s):
    # 이미 증식한 바이러스들은 주변에 바이러스가 있기 떄문에 증식 x -> 걸러 주어야 함.
    for i in range(1, k+1):
        arr, temp = spread_virus(arr, i)
    virus_idx = temp

print(arr[x-1][y-1])