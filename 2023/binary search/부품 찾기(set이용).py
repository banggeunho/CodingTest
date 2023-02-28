n = int(input())
array = set(map(int, input().split())) # 중복 제거를 위해 set 자료형 이룡

m = int(input())
finds = list(map(int, input().split()))


for i in finds:
    if i in array:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')
