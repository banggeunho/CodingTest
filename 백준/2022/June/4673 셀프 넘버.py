hasMaker = []
for i in range(1, 10001):
    result = i
    n = str(i)
    for j in n:
        result += int(j)

    hasMaker.append(result)

for i in range(1, 10001):
    if i not in hasMaker:
        print(i)
