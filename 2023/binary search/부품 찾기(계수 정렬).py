# 5
# 8 3 7 9 2
# 3
# 5 7 9


n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
finds = list(map(int, input().split()))

for i in finds:
    if array[i] == 1:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')
