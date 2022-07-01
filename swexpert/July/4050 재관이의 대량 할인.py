# 세묶음씩 묶었을때 가장 저렴한 옷은 제외하고 돈을 지불
# 즉 거꾸로 소팅해서 비싼애들부터 지워나가면 최대 할인

for tc in range(1, int(input())+1):

    n = int(input())
    prices = list(map(int, input().split()))
    prices.sort(reverse=True)

    total = 0
    for i in range(n):
        if (i+1)%3 != 0:
            total += prices[i]

    print(f'#{tc} {total}')


