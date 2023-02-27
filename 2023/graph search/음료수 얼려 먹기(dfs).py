n, m = map(int, input().split())

arr = [] # 얼음 정보 입력 받기
for i in range(n):
    arr.append(list(map(int, input())))

def dfs(x, y):
    if 0 <= x < n and 0 <= y < m and arr[x][y] == 0:
        arr[x][y] = 1 # 방문 처리
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)