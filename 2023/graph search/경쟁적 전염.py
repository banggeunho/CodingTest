from collections import deque
N, K = map(int, input().split())
arr = []
virus_places = [[] for _ in range(K+1)]
for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(N):
        if data[j] != 0:
            virus_places[data[j]].append((i, j))

S, X, Y = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def spread_virus(arr, k):
    for cx, cy in virus_places[k]:
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = k
                temp[k].append((nx, ny))

    return arr


for i in range(S):
    temp = [[] for _ in range(K+1)]
    for j in range(1, K+1):
        arr = spread_virus(arr, j)
    virus_places = temp

print(arr[X-1][Y-1])
