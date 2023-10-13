# https://www.acmicpc.net/problem/2503
from itertools import permutations
N = int(input())
num_cases = list(permutations([str(i) for i in range(1, 10)], 3))

for _ in range(N):
    num, strike, ball = map(int, input().split())
    num_str = str(num)
    remove_cnt = 0
    for i in range(len(num_cases)):
        cs = cb = 0
        i -= remove_cnt
        for j in range(3):
            if num_cases[i][j] == num_str[j]:
                cs += 1
            elif num_str[j] in num_cases[i]:
                cb += 1

        if cs != strike or cb != ball:
            num_cases.remove(num_cases[i])
            remove_cnt += 1

print(len(num_cases))