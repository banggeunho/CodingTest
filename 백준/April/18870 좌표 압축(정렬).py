# 18870 μ’ν μμΆ
n = int(input())
mapping = dict()
arr = list(map(int, input().split()))
temp = list(set(arr))
temp.sort()
for i in range(len(temp)):
    mapping[temp[i]] = i

for i in arr:
    print(mapping[i], end=' ')