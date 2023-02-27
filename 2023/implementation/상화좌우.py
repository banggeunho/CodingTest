
d = [(0, -1), (0, 1), (-1, 0), (1, 0)] # L R U D

n = int(input())
cmds = list(input().split())
cx, cy = 1, 1

for cmd in cmds:
    idx = 0
    if cmd == 'L':
        idx = 0
    elif cmd == 'R':
        idx = 1
    elif cmd == 'U':
        idx = 2
    else:
        idx = 3

    nx, ny = cx + d[idx][0], cy + d[idx][1]

    if 1<= nx <=5 and 1<= ny <= 5:
        cx, cy = nx, ny

print(cx, cy)