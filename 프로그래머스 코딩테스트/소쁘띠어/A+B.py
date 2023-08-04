# https://softeer.ai/practice/info.do?idx=1&eid=362
N = int(input())
for i in range(1, N+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')