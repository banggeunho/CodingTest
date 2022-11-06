# 코딩테스트 대비 기초 문제 풀이
# Date : 2022. 11. 6.

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****--------------------------------------------

num_dict = dict()

tmp = list(map(int, input()))

for i in tmp:
    if i in num_dict.keys():
        num_dict[i] += 1
    else:
        num_dict[i] = 1

if 6 in num_dict.keys() and 9 in num_dict.keys():
    num_dict[6] = int((num_dict[6] + num_dict[9]) / 2 + 0.5)
    num_dict[9] = 0

elif 6 in num_dict.keys():
    num_dict[6] = int(num_dict[6] / 2 + 0.5)

elif 9 in num_dict.keys():
    num_dict[9] = int(num_dict[9] / 2 + 0.5)

ans = 0
flag = False
max_num = max(num_dict.values())

for i in range(1, max_num + 1):
    flag = False
    for j in num_dict.keys():
        if num_dict[j] > 0:
            num_dict[j] -= 1
            flag = True

    if flag:
        ans += 1

print(ans)
