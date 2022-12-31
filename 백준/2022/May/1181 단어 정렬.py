n = int(input())
words = []
for _ in range(n):
    data = input()
    words.append((len(data), data))

words.sort()
prev = ''
for i in words:
    if i[1] != prev:
        print(i[1])
    prev = i[1]

# 길이순
# 단어순
# 중복출력 x

