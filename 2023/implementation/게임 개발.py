n, m = map(int, input().split())
cx, cy, dir = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 0: 동, 1: 서, 2: 남, 3: 북
# map  0: 육지, 1: 바다, 2: 가본 곳

# 동(0) -> 북(3) -> 서(1) -> 남(2) -> 동(0)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while True:

