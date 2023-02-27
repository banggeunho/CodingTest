n = int(input())

# scores = []
# for i in range(n):
#     name, score = input().split()
#     scores.append([int(score), name])
#
# print(scores)
# scores.sort()
# print(scores)
# for i in range(n):
#     print(scores[i][1], end=' ')


# 두번 째 버전
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array = sorted(array, key= lambda student: student[1])

for student in array:
    print(student[0], end=' ')