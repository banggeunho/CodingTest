# https://school.programmers.co.kr/learn/courses/30/lessons/81302?language=python3
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def is거리두기(x, y, place, visited):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        cx, cy, cost = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != 'X':
                if place[nx][ny] == 'P':
                    return False

                if cost < 1:
                    q.append((nx, ny, cost+1))
                    visited[nx][ny] = True

    return True

def solution(places):
    answer = []
    for place in places:
        visited = [[False] * 5 for _ in range(5)]
        isDone = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not visited[i][j]:
                    if not is거리두기(i, j, place, visited):
                        isDone = True
                        answer.append(0)
                        break

            if isDone:
                break

        if not isDone:
            answer.append(1)

    return answer
# def check(place):
#     n = len(place)
#     for i in range(n-2):
#         for j in range(n-2):
#             if place[i][j] == 'P':
#                 if place[i+1][j] == 'P' or  place[i][j+1] == 'P':
#                     return 0
#                 if (place[i+1][j] != 'X' or place[i][j+1] != 'X') and place[i+1][j+1] == 'P':
#                     return 0
#                 if (place[i-1][j] != 'X' or place[i+1][j] != 'X') and place[i+1][j-1] == 'P':
#                     return 0
#                 if place[i+1][j] != 'X' and place[i+2][j] == 'P':
#                     return 0
#                 if place[i][j+1] != 'X' and place[i][j+2] == 'P':
#                     return 0
#
#     return 1
#
#
# def solution(places):
#     return [check(place) for place in places]


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))