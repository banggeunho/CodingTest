import math

# 출발점과 도착점을 감싸는 원의 갯수를 세는 문제로 생각할 수 있음
# 예외상황 (둘 다 같은 원 안의 들어있을 경우 카운트 x)
# 원의 중심과의 거리가 반지름보다 작거나 같을 경우 원 안에 있는 것으로 간주 가능
for tc in range(1, int(input())+1):
    data = list(map(int, input().split()))
    sx, sy = data[0], data[1]
    dx, dy = data[2], data[3]
    n = int(input())
    count = 0
    for i in range(n):
        x, y, r = map(int, input().split())
      
        if math.sqrt(math.pow(x-sx, 2) + math.pow(y-sy, 2)) <= r and math.sqrt(math.pow(x-dx, 2) + math.pow(y-dy, 2)) <= r:
            continue
        if math.sqrt(math.pow(x-sx, 2) + math.pow(y-sy, 2)) <= r:
           count += 1
        elif math.sqrt(math.pow(x-dx, 2) + math.pow(y-dy, 2)) <= r:
           count += 1

    print(count)


