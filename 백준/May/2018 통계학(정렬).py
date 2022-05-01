# 산술평균, 중앙값, 최빈값, 범위
# 반올림-> 0.5 더한 후 math.floor 사용
# 중앙값 -> 짝수, 홀수일 경우 나눠서 출력
# 최빈값 -> counter 라이브러리 사용
# 범위는 list max,min함수 사용

from collections import Counter
import math
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
print(math.floor(sum(data)/len(data)+0.5))
if n % 2 == 0:
    print(data[n/2])
else:
    print(data[int(n/2)])

cnt = Counter(data)
temp = cnt.most_common()
maximum = temp[0][1]
modes = []
for num in temp:
    if num[1] == maximum:
        modes.append(num[0])
modes.sort()
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])
print(max(data)-min(data))




