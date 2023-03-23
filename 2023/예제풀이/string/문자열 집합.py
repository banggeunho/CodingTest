N, M = map(int, input().split())

string_set = set()
for _ in range(N):
    string_set.add(input())

result = 0
for _ in range(M):
    data = input()
    if data in string_set:
        result += 1

print(result)
