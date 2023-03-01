

dirs = [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

cur = list(input())
cx, cy = int(cur[1]) - 1, ord(cur[0])-ord('a')

result = 0
for dir in dirs:
    nx, ny = cx + dir[0], cy + dir[1]
    if 0 <= nx < 8 and 0 <= ny < 8:
        result += 1

print(result)
        