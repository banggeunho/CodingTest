# https://www.acmicpc.net/problem/17140
from collections import defaultdict

R, C, K = map(int, input().split())
R = R - 1
C = C - 1

A = [list(map(int, input().split())) for _ in range(3)]

def c_computation():
    max_num = 0
    temp_list = []
    for i in range(len(A[0])):
        temp = []
        temp_dict = defaultdict(int)
        for j in range(len(A)):
            if A[j][i] == 0:
                continue
            temp_dict[A[j][i]] += 1

        for num in sorted(list(temp_dict.keys()), key=lambda x: [temp_dict[x], x]):
            temp.extend([num, temp_dict[num]])

        max_num = max(max_num, len(temp))
        temp_list.append(temp)
        # print(temp_list)

    # 채우기
    for i in range(len(temp_list)):
        temp_list[i].extend([0] * (max_num - len(temp_list[i])))
        if len(temp_list) > 100:
            temp_list[i] = temp_list[i][:100]

    result_list = []
    for i in range(len(temp_list[0])):
        temp = []
        for j in range(len(temp_list)):
            temp.append(temp_list[j][i])
        result_list.append(temp)

    return result_list

def r_computation():
    max_num = 0
    temp_list = []
    for i in range(len(A)):
        temp = []
        temp_dict = defaultdict(int)
        for j in range(len(A[0])):
            if A[i][j] == 0:
                continue
            temp_dict[A[i][j]] += 1

        for num in sorted(list(temp_dict.keys()), key=lambda x: [temp_dict[x], x]):
            temp.extend([num, temp_dict[num]])

        temp_list.append(temp)
        max_num = max(max_num, len(temp_list[i]))

    # 채우기
    for i in range(len(temp_list)):
        temp_list[i].extend([0] * (max_num - len(temp_list[i])))
        if len(temp_list[i]) > 100:
            temp_list[i] = temp_list[i][:100]

    return temp_list


if 0 <= R < len(A) and 0 <= C < len(A[0]) and A[R][C] == K:
    print(0)

else:
    time = 0
    while True:

        if time > 100:
            print(-1)
            break

        # print(A)
        if 0 <= R < len(A) and 0 <= C < len(A[0]) and A[R][C] == K:
            print(time)
            break

        time += 1

        if len(A) >= len(A[0]):
            A = r_computation()
        else:
            A = c_computation()
