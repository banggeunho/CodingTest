# 1654 랜선 자르기
# 랜선을 자를 수 있는 최소 크기(0)을 start로 선정
# 랜선을 자를 수 있는 최대의 크기를 end로 선정

# end를 줄이면 자른 랜선의 갯수가 늘어감
# start를 늘리면 자른 랜선의 갯수가 줄어듬
k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

start = 0
end = max(arr)

while start <= end:
    mid = (start+end) // 2
    result = 0
    for i in arr:
        if mid == 0:
            result += i
        else:
            result += (i // mid)

    if result >= n:
        start = mid + 1

    else:
        end = mid - 1

print(end)