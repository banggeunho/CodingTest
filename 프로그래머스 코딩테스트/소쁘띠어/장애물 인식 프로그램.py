# https://softeer.ai/practice/info.do?idx=1&eid=409&sw_prbl_sbms_sn=236876
import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
answer = []

def search_blocks(q):
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
    return cnt

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            answer.append(search_blocks(deque([(i, j)])))

print(len(answer))
for num in sorted(answer):
    print(num)

