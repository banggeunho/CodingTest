h, w, x, y = map(int, input().split())
b = []
a = [[0]*w for _ in range(h)]
for _ in range(h+x):
    b.append(list(map(int, input().split())))

# 맨 첨
for i in range(h):
    for j in range(w):
        if i - x >= 0 and j - y >= 0:
            a[i][j] = b[i][j] - a[i-x][j-y]
        else:
            a[i][j] = b[i][j]

    for j in range(w):
        print(a[i][j], end=' ')
    print()



