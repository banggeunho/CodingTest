# 숫자가 같으면 그때부터 슬라이드 윈도우로 탐색

# 방향이 뒤집어 졌을때도 고려해서 탐색

n = int(input())
standard = list(map(int, input().split()))
m = int(input())

import copy
def trans(arr):
    k = {1: 3, 2:4, 3:1, 4:2}
    temp = copy.deepcopy(arr)
    for i in range(n):
        temp[i] = k[arr[i]]

    temp.reverse()
    return temp

answers = []
for _ in range(m):
    temp = list(map(int, input().split()))
    reverse_temp = trans(temp)
    solve = False

    if not solve:
        for i in range(n):
            solve = True
            cnt = 0
            k = i
            for j in range(n):
                if standard[k % n] == temp[j]:
                    solve = True
                    cnt += 1
                    k += 1
                else:
                    cnt = 0
                    break

            if cnt != n:
                solve = False

            if solve:
                answers.append(temp)

    if not solve:
        for i in range(n):
            solve = True
            cnt = 0
            k = i
            for j in range(n):
                if standard[k % n] == reverse_temp[j]:
                    # print(k, j)
                    cnt += 1
                    k += 1
                else:
                    cnt = 0
                    break

            if cnt != n:
                solve = False

            if solve:
                answers.append(temp)
                break

print(len(answers))
for i in range(len(answers)):
    for j in range(n):
        print(answers[i][j], end= ' ')
    print()





