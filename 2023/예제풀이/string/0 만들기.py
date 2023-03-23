# https://www.acmicpc.net/problem/7490

for _ in range(int(input())):
    n = int(input())
    answer = []
    arr = ['1']
    def dfs(num):
        # print(arr)
        if num == n:
            result = ''.join(arr)
            temp = result
            if ' ' in result:
                result = result.replace(' ', '')

            if eval(result) == 0:
                answer.append(temp)
            return

        arr.append(' '+str(num+1))
        dfs(num+1)
        arr.pop()

        arr.append('+'+str(num+1))
        dfs(num+1)
        arr.pop()

        arr.append('-'+str(num+1))
        dfs(num+1)
        arr.pop()

    dfs(1)

    for ans in answer:
        print(ans)

    print()
