n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
while start <= end:
    temp = 0
    mid = (start+end) // 2 # 블루레이의 최소 크기를 계속해서 찾아 나간다.

    for i in range(n):
        tree = arr[i] - mid
        if tree < 0:
            tree = 0
        temp += tree
        if temp >= m: # 잘려진 나무가 중간에 원하는 나무보다 커질 경우 탈출
            break

    if temp >= m: # 원하는 길이보다 클 경우 start를 올려 절단기의 높이를 올림 -> 잘리는 나무의 길이가 작아짐
        start = mid + 1
        
    else: # 원하는 길이보다 작을 경우 end를 줄여 절단기의 높이를 내림 -> 잘리는 나무의 길이가 커짐
        end = mid - 1

print(end)