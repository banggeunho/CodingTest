n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((y, x))

for y, x in sorted(arr):
    print(x, y)

# y 좌표 증가 순
# x 좌표 증가 순