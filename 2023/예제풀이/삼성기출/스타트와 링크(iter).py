import itertools
n = int(input())
numbers = [i for i in range(1, n+1)]
S=[list(map(int, input().split())) for _ in range(n)]

cases = itertools.combinations(numbers, n//2)
result = int(1e9)
for case in cases:
    star_score = 0
    link_score = 0
    star = list(case)
    link = [i for i in numbers if i not in list(case)]
    # print(star, link)

    for i in range(len(star)-1): # 스타 팀 능력치 구하기
        for j in range(i+1, len(star)):
            star_score += S[star[i]-1][star[j]-1]
            star_score += S[star[j]-1][star[i]-1]

    for i in range(len(link)-1): # 링크 팀 능력치 구하기
        for j in range(i+1, len(link)):
            link_score += S[link[i]-1][link[j]-1]
            link_score += S[link[j]-1][link[i]-1]


    # print(star_score, link_score)
    result = min(result, abs(star_score - link_score))

print(result)