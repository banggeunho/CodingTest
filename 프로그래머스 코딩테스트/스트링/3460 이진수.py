for tc in range(int(input())):

    n = int(input())
    # b -> 2진수
    # o -> 8진수
    # x -> 16진수
    # d -> 10진수
    binaryNum = format(n, 'b')[::-1] # bin(n)[2:][::-1]
    print(binaryNum)
    for i in range(len(binaryNum)):
        if binaryNum[i] == '1':
            print(i, end=' ')

    print()