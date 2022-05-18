n, m = map(int, input().split())
k = int(input())

vertical = [0, m]
horizontal = [0, n]

for _ in range(k):
    a, b = map(int, input().split())
    if a == 0:
        vertical.append(b)
    else:
        horizontal.append(b)

vertical.sort()
horizontal.sort()

vertical_new = []
horizontal_new = []
for i in range(len(vertical)-1):
    vertical_new.append(vertical[i+1] - vertical[i])

for i in range(len(horizontal)-1):
    horizontal_new.append(horizontal[i+1] - horizontal[i])

ans = 0
for i in range(len(vertical_new)):
    for j in range(len(horizontal_new)):
        ans = max(ans, vertical_new[i]*horizontal_new[j])

print(ans)






