# 1697 숨바곡질
from collections import deque
n, k = map(int, input().split())
distance =[987654321]*100001 # 방문과 거리노드

def bfs(start, cost):
    global distance
    q = deque()
    q.append((start, cost)) # 시작지점, 비용 (초기 0)
    distance[start] = 0
    while q:
        now, sec = q.popleft()
        if sec > distance[now]: # 현재 뽑은 거리가 distance 노드에 있는 거리보다 클 경우
            continue

        if now == k: # 원하는 지점 도달 시 탈출
            break

        if 0 <= now - 1 < 100001 and distance[now-1] > sec+1: # 범위 안에 있으면서 이 새끼 보다 내가 더 작을 경우
            distance[now-1] = sec+1
            q.append((now-1, sec+1))
        if 0 <= now + 1 < 100001 and distance[now+1] > sec+1:
            distance[now+1] = sec + 1
            q.append((now+1, sec+1))
        if 0 <= now * 2 < 100001 and distance[now*2] > sec+1:
            distance[now*2] = sec + 1
            q.append((now*2, sec+1))

bfs(n, 0)
print(distance[k])