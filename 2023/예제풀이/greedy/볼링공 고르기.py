n, m = map(int, input().split())
data = list(map(int, input().split()))

ball = [0] * 11

for x in data:
    ball[x] += 1 # 무게별로 공 추가

result = 0
for i in range(1, m + 1):
    n -= ball[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += ball[i] * n # b가 선택할 수 있는 경우의 수와 곱하기

print(result)


