

def dfs(idx, now, operand_cnt):
    global  max_val, min_val
    if idx == n:
        max_val = max(max_val, now)
        min_val = min(min_val, now)
        return now

    for i in range(4):
        if operand_cnt[i] > 0:
            operand_cnt[i] -= 1
            if i == 0: # 덧셈
                dfs(idx+1, now + arr[idx], operand_cnt)
            elif i == 1: # 뺼셈
                dfs(idx+1, now - arr[idx], operand_cnt)
            elif i == 2: # 곱셈
                dfs(idx+1, now * arr[idx], operand_cnt)
            else:
                dfs(idx+1, int(now / arr[idx]), operand_cnt)
            operand_cnt[i] += 1

n = int(input())
arr = list(map(int, input().split()))
operand_cnt = list(map(int, input().split()))
max_val = -int(1e9)
min_val = int(1e9)


dfs(1, arr[0], operand_cnt)
print(max_val)
print(min_val)
