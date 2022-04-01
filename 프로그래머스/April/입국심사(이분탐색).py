# 심사에 걸리는 시간을 이분 탐색 범위로 지정
# right 부분은 최대 걸리는 시간으로 지정
# mid를 걸린 시간으로 간주하여 최적의 시간을 찾아 나가는 알고리즘
# mid와 심사관들의 시간을 나누어 몇명을 심사했는지 구한 후 주어진 n명보다 많거나 적을 경우 조건을 주어 이분탐색을 이어간다.

def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for time in times:
            people += mid // time
            
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            end = mid - 1
            
        elif people < n:
            start = mid + 1
            
    return answer