# 곱하기 혹은 더하기
# 수를 배열로 만들어 결과를 인덱스 0 값으로 설정 후
# 인덱스 1부터 리스트 끝까지 살펴보면서 전 인덱스의 값이 0또는 1이면
# 더하기를 하도록, 나머지 수들에 대해서는 곱하기를 수행

arr = list(map(int, input()))

result = arr[0]
for i in range(1, len(arr)):
    if arr[i-1] == 0 or arr[i-1] == 1:
        result += arr[i]
    else:
        result *= arr[i]

print(result)


