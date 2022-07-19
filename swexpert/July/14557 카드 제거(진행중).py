def dfs(data):
    count = 0
    is_one = False
    print(data)
    for i in range(len(data)):
        if data[i] == '2':
            count += 1

        if data[i] == '1':
            is_one = True
            data[i] = '2'
            if i > 0:
                if data[i - 1] == '0':
                    data[i - 1] = '1'
                elif data[i - 1] == '1':
                    data[i - 1] = '0'

            if i < len(data) - 1:
                if data[i + 1] == '0':
                    data[i + 1] = '1'
                elif data[i + 1] == '1':
                    data[i + 1] = '0'

            return dfs(data)

    if count == len(data):
        return "yes"
    else:
        if not is_one:
            return "no"

for tc in range(1, int(input())+1):
    data = list(input())
    print(f'#{tc} {dfs(data)}')