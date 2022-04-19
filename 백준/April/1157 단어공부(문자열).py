# 문장이 주어졌을때 제일 많이 등장한 단어 출력
# 대소문자 구별 X , 출력은 대문자로 -> 대문자로 다 바꿔준다
# 최대값이 여러개일 경우 물음표 출력

data = input()
data = data.upper()
answer = {}
alphabet = list(set(data))
for alpha in alphabet:
    count = data.count(alpha)
    answer[alpha] = count

if list(answer.values()).count(max(answer.values())) > 1:
    print('?')
else:
    for a in alphabet:
        if answer[a] == max(answer.values()):
            print(a)