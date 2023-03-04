# 1.국어 점수가 감소하는 순서로
# 2, 영어 점수가 증가하는 순서
# 3. 수학 점수가 감소하는 순서로
# 4. 이름이 사전순 증가

n = int(input())
arr = []
for _ in range(n):
    data = list(input().split())
    arr.append((data[0], int(data[1]), int(data[2]), int(data[3])))

arr.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(arr[i][0])
