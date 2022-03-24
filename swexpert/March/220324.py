# 1221. [S/W 문제해결 기본] 5일차 - GNS
digit= ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d = dict(zip(digit, idx))
for tc in range(1, int(input())+1):
    arr = list(input().split())
    n = int(arr[1])
    data = list(input().split())
    for i in range(n):
        data[i] = d.get(data[i])
    data.sort()
    r_d = dict(map(reversed, d.items()))
    print(f'#{tc}')
    for i in range(n):
        print(r_d.get(data[i]), end=' ')
    print()