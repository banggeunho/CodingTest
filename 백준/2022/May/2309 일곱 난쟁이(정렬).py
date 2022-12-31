import itertools
data = []
for i in range(9):
    data.append(int(input()))
cases = itertools.combinations(data, 7)
for case in cases:
    if sum(list(case)) == 100:
        for i in sorted(list(case)):
            print(i)
        break

# 9명의 난쟁이 중 7명이 되는 모든 케이스를 골라
# 키가 100이 되는 경우를 오름차순 정렬 후 출력




