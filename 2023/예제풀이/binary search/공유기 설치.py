n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))

house.sort()

def search_max_distance(start, end, result):

    if start > end:
        return result

    mid = (start + end) // 2
    count = 1
    value = house[0]

    for i in range(1, n): # 공유기 설치 => 설치 후 최근 설치된 집 변경
        if house[i] >= value + mid:
            count += 1
            value = house[i]

    if count >= c: # 설치할 수 있는 공유기 수가 많으면 -> 최대 거리를 더 늘려서 공유기 수를 줄인다.
        return search_max_distance(mid + 1, end, mid)

    else:
        return search_max_distance(start, mid - 1, result)

print(search_max_distance(1, house[-1]-house[0], 1))
