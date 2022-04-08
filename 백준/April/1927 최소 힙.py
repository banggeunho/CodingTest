# 우선순위 큐 구현 문제
import heapq
q = []
n = int(input())
answer = []
for i in range(n):
  data = int(input())
  if data == 0:
    if len(q) < 1:
      heapq.heappush(q, data)
    answer.append(heapq.heappop(q))
  else:
    heapq.heappush(q, data)

for i in answer:
  print(i)