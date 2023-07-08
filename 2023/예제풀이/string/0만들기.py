answers = []
def dfs(n, depth, string):
    if depth == n:
        if eval(string.replace(' ', '')) == 0:
            # print(string)
            answers.append(string)
        return

    else:
        dfs(n, depth+1, string + '+' + str(depth + 1))
        dfs(n, depth+1, string + '-' + str(depth + 1))
        dfs(n, depth+1, string + ' ' + str(depth + 1))


for _ in range(0, int(input())):
    n = int(input())

    dfs(n, 1, "1")

    for ans in sorted(answers):
        print(ans)

    answers.clear()
    print()


