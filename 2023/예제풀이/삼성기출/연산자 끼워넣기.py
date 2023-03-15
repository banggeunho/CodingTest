n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -(int(1e9))
min_value = int(1e9)


def dfs(total, step):
    global max_value, min_value, add, sub, mul, div

    if step == n - 1:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return

    if add > 0:
        add -= 1
        dfs(total+arr[step+1], step+1)
        add += 1

    if sub > 0:
        sub -= 1
        dfs(total-arr[step+1], step+1)
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(total*arr[step+1], step+1)
        mul += 1

    if div > 0:
        div -= 1
        dfs(int(total/arr[step+1]), step+1)
        div += 1

dfs(arr[0], 0)

print(max_value)
print(min_value)








