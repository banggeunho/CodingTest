from collections import defaultdict
N, M, K = map(int, input().split())
fireballs = []

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1, m, s, d))

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for i in range(K):
    # 모든 파이어볼을 방향으로 속력만큼 이동한다.
    newFireballs = defaultdict(list)
    for r, c, m, s, d in fireballs:
        dr, dc = directions[d]
        nr = (r + (dr * s)) % N
        nc = (c + (dc * s)) % N
        newFireballs[(nr, nc)].append((nr, nc, m, s, d))

    fireballs = []
    for location in newFireballs:
        # 같은 위치에 2개이상 파이어볼이 위치할 경우 합친다.
        if len(newFireballs[location]) >= 2:
            sum_m, sum_s = 0, 0
            x, y = location

            for fireball in newFireballs[location]:
                _, _, m, s, _ = fireball
                sum_m += m
                sum_s += s

            # 모두 방향이 짝수이거나, 홀수이면 방향은 0, 2, 4, 6 아니면 1, 3, 5, 7
            all_even = all(fireball[4] % 2 == 0 for fireball in newFireballs[location])
            all_odd = all(fireball[4] % 2 != 0 for fireball in newFireballs[location])
            newDirections = [i * 2 if all_even or all_odd else (i + 1) * 2 - 1 for i in range(4)]

            for j in range(4):
                # 2-4. 질량이 0인 파이어볼은 소멸되어 없어진다.
                if (sum_m // 5) > 0:
                    fireballs.append((x, y, sum_m // 5, sum_s // len(newFireballs[location]), newDirections[j]))

        else:
            fireballs.extend(newFireballs[location])

# 모든 질량의 합을 구하기
result = sum(fireball[2] for fireball in fireballs)

print(result)
