# https://www.acmicpc.net/problem/12919
# BFS 이용 버전
from collections import deque
S = input()
T = input()
solve = False

def bfs(string):
    global solve
    q = deque()
    q.append(string)

    while q:
        now_string = list(q.popleft())
        if len(S) > len(now_string):
            break

        if S == ''.join(now_string):
            solve = True
            break

        if now_string[-1] == 'A':
            now_string.pop()
            q.append(''.join(now_string))
            now_string.append('A')

        if now_string[0] == 'B':
            now_string = now_string[::-1]
            now_string.pop()
            q.append(''.join(now_string))

bfs(T)
print(1 if solve else 0)
