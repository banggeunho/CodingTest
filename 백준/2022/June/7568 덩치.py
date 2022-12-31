n = int(input())
# (x, y) , (p, q) x > p and y > q 이면 a가 b보다 덩치가 더 크다.
# n명의 집단에서는 각 사람의 덩치 등수는 자신보다 더 큰덩치 사람의 수
# k명이 나보다 더 크면 자기는 k+1등이 되는 법

data = []
for _ in range(n):
    w, h = map(int, input().split())
    data.append((w, h))

result = []
for i in range(len(data)):
    t_w, t_h = data[i][0], data[i][1]
    count = 0
    for j in range(len(data)):
        if i == j: continue
        else:
            if t_w < data[j][0] and t_h < data[j][1]:
                count += 1

    result.append(count+1)

for i in result:
    print(i, end=' ')