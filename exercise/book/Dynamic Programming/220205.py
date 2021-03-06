# 코딩테스트 대비 기초 문제 풀이 17일차
# Date : 2022. 02. 04.
# 다이내믹 프로그래밍(DP))

# 다이나믹 프로그래밍(동적 계획법) // 문제풀이

# 개미 전사
# 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.
# 첫째줄엔 식량창고 N개가 주어진다
# 둘째줄엔 식량창고에 저장된 식량의 갯수가 주어진다.

n = int(input())
k = list(map(int, input().split()))
d = [0] * 1001

# I번쨰의 최적의 해를 구할 때 왼쪽부터 i-3 번쨰 이하에 대한 최적의 해에 대해서는 고려할 필요가 없음
# -> 예를들어 d[i-3]은 d[i-1]와 d[i-2]를 구하는 과정에서 이미 고려되었기 때문에
# -> i번쨰의 최적의 해를 구할 때는 d[i-1]와 d[i-2]를 고려하면 된다
# i번 째는 i-1를 들리지 못하고, i-2 + 현재위치를 한 값이 전에 위치의 최적의 해보다 높은지 작은지 판단
# A(i) = max(A(i-1), A(i-2) + k(i))
# DP (BOTTOM - UP)
d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])


# 바닥 공사
# 가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다.
# 이 바닥을 1X2의 덮게, 2X1의 덮개, 2X2의 덮개를 이용해 채우고자 한다.

# 첫째 줄에 N이 주어진다 ( 1 <= N <= 1000)
# 첫째 줄에 2 X N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력한다.

# 핵심
# 왼쪽부터 i-1번째까지 길이가 덮개로 이미 채워져 있으면 2x1의 덮개를 채우는 하나의 경우의 수가 전부
# i-2번째까지 길이가 덮개로 이미 채워져 있으면 1 x 2 덮개를 2개 넣는 경우, 2 x 2덮개 하나를 넣는 경우로 2가지 가능
# 점화식 : A(i) = A(i-1) + A(i-2) * 2
n = int(input())

d = [0] * 1001

d[0] = 1
d[1] = 3
for i in range(2,n+1):
  d[i] = (d[i-1] + 2*d[i-2]) % 796796

print(d[n-1])