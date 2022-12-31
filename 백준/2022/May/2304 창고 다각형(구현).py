n = int(input())

data = []
max_height = 0
max_index = 0
max_left = 0
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

    # 최대 인덱스, 최대길이인 부분 구하기
    if max_left < a:
        max_left = a
    if max_height < b:
        max_height = b
        max_index = a

result = 0
kkk = [0] * (max_left + 1) # 각 넓이를 담을 리스트 초기엔 0으로 초기화
for l, h in data:
    kkk[l] = h # 각 지붕을 달아준다

temp = 0
for i in range(max_index + 1): # 제일 높은 새1끼까지 확인
    if kkk[i] > temp:
        temp = kkk[i]
    result += temp

temp = 0
for i in range(max_left, max_index, -1): # 제일 높은 새1끼 전까지 반대로 확인
    if kkk[i] > temp:
        temp = kkk[i]
    result += temp

print(result)



