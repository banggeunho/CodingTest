n, m = map(int, input().split())
arr = list(map(int, input().split()))


start = max(arr) # 블루레이 하나 당 한개의 강의를 각각 담을 수 있는 크기
end = sum(arr) # 블루레이의 하나로 다 담을 수 있는 크기(경우)

while start <= end:
    temp, cnt = 0, 0 # 각 블루레이의 합, 블루레이의 갯수
    mid = (start+end) // 2 # 블루레이의 최소 크기를 계속해서 찾아 나간다.

    for i in range(n):
        if temp + arr[i] > mid: # 지정한 최소 크기보다 값이 커질 경우
            temp = 0
            cnt += 1
        temp += arr[i] # 지정한 최속 크기보다 값이 적으면 계속해서 더한다.

    if temp !=0: cnt += 1 # 마지막 값 처리

    if cnt <= m: # 블루레이 갯수가 지정한 갯수가보다 같거나 적을 경우
        end = mid - 1

    else: # 블루레이 갯수가 지정한 갯수보다 클 경우
        start = mid + 1

print(start)