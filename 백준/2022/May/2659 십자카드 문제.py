data = list(map(int, input().split()))
# 시계 수 찾기
def findTimeNum(data):
    time_num = 10000
    for i in range(4):
        start = data[i]
        result = start
        for j in range(1, 4):
            idx = (i+j)%4
            result *= 10
            result += data[idx]
        time_num = min(time_num, result)
    return time_num

answer = findTimeNum(data)
start = 1111
cnt = 1
save = []
for i in range(start, 10000):
    data = list(str(i))
    data = [int(i) for i in data]
    if 0 in data:
        continue

    temp = findTimeNum(data)
    if temp in save:
        continue
    else:
        save.append(temp)
        if answer == temp:
            break
        cnt += 1
print(cnt)