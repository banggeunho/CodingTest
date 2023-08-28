# https://school.programmers.co.kr/learn/courses/30/lessons/49191
from collections import defaultdict

def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)

    for winner, loser in results:
        win[loser].add(winner)
        lose[winner].add(loser)

    for i in range(1, n + 1):
        for winner in win[i]:
            lose[winner].update(lose[i])

        for loser in lose[i]:
            win[loser].update(win[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer


def solution(n, results):
    answer = 0
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for a, b in results:
        graph[a][b] = 1  # 이겼다
        graph[b][a] = -1  # 졌다

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a != b and graph[a][b] == 0:
                    # a <- k <- b  ==  a <- b (이겼을때)
                    if graph[a][k] == 1 and graph[k][b] == 1:
                        graph[a][b] = 1
                    elif graph[a][k] == -1 and graph[k][b] == -1:
                        graph[a][b] = -1

    for i in range(1, n + 1):
        # 자기자신만 0일때(즉, 나머지 노드랑 순위관계가 있음)
        if graph[i][1:].count(0) == 1:
            answer += 1

    return answer