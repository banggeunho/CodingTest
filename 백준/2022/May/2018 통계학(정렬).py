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
print(data[n//2])
temp = Counter(data).cnt.most_common()

if len(temp) > 1:
  if temp[0][1] == temp[1][1]:
    print(temp[1][0])
  else:
    print(temp[0][0])
else:
  print(temp[0][0])
  
print(data[-1] - data[0])




