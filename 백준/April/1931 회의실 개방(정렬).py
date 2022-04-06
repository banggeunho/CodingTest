#1931 회의실 배정
# 회의 종료시간이 제일 짧은 순으로 정하면 되겠다!!!!

# 회의 시작 시간이 동일한 경우 까지 고려해서
# sort를 시작시간 -> 종료시간 순으로 2번 시행
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:x[0])
arr.sort(key = lambda x:x[1])
cnt = 1
end = arr[0][1]
for i in range(1, n):
    if end <= arr[i][0]:
        cnt += 1
        end = arr[i][1]
print(cnt)