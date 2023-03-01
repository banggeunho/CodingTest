# 모든 수를 0으로 뒤집었을 때, 1로 뒤집었을 때 비교
arr = list(map(int, input()))

cnt_0 = 0
cnt_1 = 0
# 첫번째 수 처리
if arr[0] == 0:
  cnt_0 += 1
else:
  cnt_1 += 1

for i in range(1, len(arr)):
    if arr[i-1] != arr[i]:
        if arr[i] == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1

print(min(cnt_0, cnt_1))