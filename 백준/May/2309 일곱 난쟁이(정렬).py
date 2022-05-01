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






