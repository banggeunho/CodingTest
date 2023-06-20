import copy
from itertools import combinations
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
arr = []
places_idx = []
virus_idx = []
for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(M):
        if data[j] == 0:
            places_idx.append((i, j))
        elif data[j] == 2:
            virus_idx.append((i, j))

cases = combinations(places_idx, 3)

def spreadVirus(arr, i, j):
    q = deque()
    q.append((i, j))

    count = 0
    while q:
        count += 1
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                    arr[nx][ny] = 2

    return arr

def countSafetyZone(arr):
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1

    return count

result = 0
for case in cases:
    tempArr = copy.deepcopy(arr)
    for i, j in case:
        tempArr[i][j] = 1

    for i, j in virus_idx:
        tempArr = spreadVirus(tempArr, i, j)

    result = max(result, countSafetyZone(tempArr))

print(result)