# 코딩테스트 대비 기초 문제 풀이 29일차
# Date : 2022. 02. 16.
# 그리디 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 무지의 먹방 라이브 (그리디 문제 -> 우선순위 큐 활용)
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
        
    sum_values = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    
    length = len(food_times)
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_values + ((q[0][0] - previous) * length) <= k:
        # 제일 적게 걸리는 음식 시간을 pop 한다.
        now = heapq.heappop(q)[0]
        # 꺼내온 음식과 이전에 다 먹은 음식 시간을 빼고 남은 음식 개수를 곱한다.
        sum_values += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x:x[1]) # 음식의 번호 기준으로 정렬하고, 리스트로 만듦
    return result[(k - sum_values) % length][1] # 전체 시간 중 sum_value를 빼고 남은 음식으로 로테이션 돌린다.

print(solution([8, 6, 4], 15))