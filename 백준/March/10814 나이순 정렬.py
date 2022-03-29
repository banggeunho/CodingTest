# 입력 받을 때 입력 받는 순서도 같이 list에 저장하고
# 두번째로 넣어줘서 정렬의 기준으로 잡히도록 설정
n = int(input())
arr = []
for i in range(n):
    data = list(input().split())
    arr.append((int(data[0]), i, data[1]))
arr.sort()
# print(arr)
for i,_,j in arr:
    print(i, j)
