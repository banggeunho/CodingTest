# 숫자로 생각하지말고 문자로 생각하기
# n은 최대 10 k는 최대 4 10P4 해도= 10!/6!
# 충분하다~

n = int(input())
k = int(input())
card = [] # 입력받은 카드 담는 list
result = [] # 만들어진 정수 담는 list
for i in range(n):
    card.append(input())

import itertools
cases = itertools.permutations(card, k)
for case in cases:
    temp = ''
    for i in range(len(case)):
        temp += case[i]

    if temp not in result:
        result.append(temp)

print(len(result))







