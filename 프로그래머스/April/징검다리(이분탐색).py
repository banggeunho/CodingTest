# 이분탐색 범위(mid)를 바위 사이에 거리 최솟값으로 설정해준다.
# 바위와 현재 위치 사이의 거리보다 거리 최솟값이(mid) 더 클경우 없는 바위로 간주 (삭제 처리)
# 최솟값(mid)과 같거나 긴 경우 거리 중 최솟값을 찾는다.
# 제거한 바위가 많을 경우 right 부분을 mid-1로 줄이고
# 제거한 바위가 적을 경우 left 부분을 mid+1로 늘인다.

def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)
    
    start, end = 0, distance
    while start <= end:
        mid = (start+end) // 2 # 거리의 최솟값을 mid로 설정
        current = 0
        remove_rocks = 0
        min_distance = int(1e9)
        
        for rock in rocks:
            diff = rock - current
            if diff < mid: # 최솟값 보다 작을 경우
                remove_rocks += 1
            else: # mid 보다 거리가 길거나 거리가 같으면 제거 x
                current = rock # 현재 위치를 그 바위로 옮김
                min_distance = min(min_distance, diff)
                
        if remove_rocks > n: # 삭제한 바위가 주어진 갯수 보다 많을 경우
            end = mid - 1
        else:
            answer = min_distance
            start = mid + 1
            
    return answer