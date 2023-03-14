import math
n = int(input())
rooms = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for people in rooms:
    people -= b
    result += 1

    if people > 0:
        result += (math.ceil(people/c))


print(result)

