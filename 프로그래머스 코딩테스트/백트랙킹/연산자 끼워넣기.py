# https://www.acmicpc.net/problem/14888
N = int(input())
nums = list(map(int, input().split()))
operand_cnt = list(map(int, input().split()))
max_result = -int(1e9)
min_result = int(1e9)
def dfs(now, idx, operand_cnt):
    global max_result, min_result

    if idx == N:
        print(now)
        max_result = max(max_result, now)
        min_result = min(min_result, now)
        return

    if operand_cnt[0] > 0:
        operand_cnt[0] -= 1
        dfs(now + nums[idx], idx + 1, operand_cnt)
        operand_cnt[0] += 1

    if operand_cnt[1] > 0:
        operand_cnt[1] -= 1
        dfs(now - nums[idx], idx + 1, operand_cnt)
        operand_cnt[1] += 1

    if operand_cnt[2] > 0:
        operand_cnt[2] -= 1
        dfs(now * nums[idx], idx + 1, operand_cnt)
        operand_cnt[2] += 1

    if operand_cnt[3] > 0:
        operand_cnt[3] -= 1
        dfs(int(now / nums[idx]), idx + 1, operand_cnt)
        operand_cnt[3] += 1

dfs(nums[0], 1, operand_cnt)

print(max_result, min_result)
