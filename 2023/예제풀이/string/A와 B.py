# 백트랙킹 사용 시 시간초과 남요
# 역순으로 생각했으면 쉽게 해결할 문제...

S = input()
T = list(input())
solve = False

while len(S) < len(T):

    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]

print(1 if S == ''.join(T) else 0)