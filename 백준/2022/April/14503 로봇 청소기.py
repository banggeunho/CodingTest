# 구현 문제
# 방향 전환을 왼쪽으로 하기 때문에 dx, dy의 설정을 고려해서 잘 해줘야 함
# 나머지는 문제의 조건에 맞게 작성하면 된다.

n, m = map(int, input().split())
arr = []
cleaned = [[0]*m for _ in range(n)]
x, y, d = map(int, input().split())

for _ in range(n):
    arr.append(list(map(int, input().split())))

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cleaned[x][y] = 1
result = 1

while True:
    flag = 0
    for _ in range(4):
        nx = x + dx[(d + 3) % 4]
        ny = y + dy[(d + 3) % 4]
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d + 3) % 4
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            if cleaned[nx][ny] == 0:
                cleaned[nx][ny] = 1
                result += 1
                x = nx
                y = ny
                # 청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break

    if flag == 0:  # 4방향 모두 청소가 되어 있을 때,
        if arr[x - dx[d]][y - dy[d]] == 1:  # 후진했는데 벽
            print(result)
            break

        else:
            x, y = x - dx[d], y - dy[d]