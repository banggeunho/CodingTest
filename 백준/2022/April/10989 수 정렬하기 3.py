# 10989 수 정렬하기 3
# 계수 정렬(count sort)
import sys
n = int(input())
arr = [0] * 10001
for i in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(arr[i]):
        print(i)
