import math
for tc in range(1, int(input())+1):
    n, d = map(int, input().split())
    print(f'#{tc} {math.ceil(n/(d*2+1))}')



