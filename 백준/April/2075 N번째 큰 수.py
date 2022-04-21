#2075 N번째 큰 수
import heapq
n = int(input())
q = []
# 밀어내기 식으로 우선순위 큐를 최신화
for i in range(n):
    data = list(map(int, input().split()))
    for j in data:
        if len(q) < n: # 우선순위 큐는 무조건 5개씩 맞춰준다.
            heapq.heappush(q, j)
        else:
            if q[0] < j: # q[0]은 현재 큐안의 최솟값, j는 입력된 숫자
                heapq.heappop(q)
                heapq.heappush(q, j)

print(q[0]) # 제일 큰 새끼들 중에서 맨 첫번째가 제일 작 은새!끼