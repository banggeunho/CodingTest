import heapq

def solution(food_times, k):

    if sum(food_times)  <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # 음식 먹는 시간, 음식 번호

    sum_values = 0 # 음식을 먹은 전체 시간
    previous = 0 # 이전의 음식을 먹은 시간
    length = len(food_times) # 현재 남은 음식의 갯수

    while sum_values + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_values += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_values) % length][1]

print(solution([3, 1, 2], 5))




