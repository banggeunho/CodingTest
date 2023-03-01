n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]: # 작을 경우인 경우 스왑 진행
        a[i], b[i] = b[i], a[i]
    else: # a의 원소가 b의 원소보다 크거나 같을 때, 반복문 탈출
        break

print(sum(a))