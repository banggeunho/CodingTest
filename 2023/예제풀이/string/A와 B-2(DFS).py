# https://www.acmicpc.net/problem/12919
# DFS 이용 버전
S = input()
T = list(input())
solve = False

def dfs(string):
    global solve
    if len(S) == len(string) or solve:
        if ''.join(string) == S:
            solve = True
        return

    if string[-1] == 'A':
        string.pop()
        dfs(string)
        string.append('A')

    if string[0] == 'B':
        string = string[::-1]
        string.pop()
        dfs(string)

dfs(T)
print(1 if solve else 0)