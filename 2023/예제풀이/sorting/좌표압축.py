n = int(input())
arr = list(map(int, input().split()))
temp = {}

for idx, i in enumerate(sorted(set(arr))):
    if i not in temp:
        temp[i] = idx

for i in arr:
    print(temp[i], end=' ')
