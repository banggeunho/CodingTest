# 모든 사진 틀은 비어있다.
N = int(input())

gallery = []

# 학생 수
K = int(input())

# 추천 리스트
recommends = list(map(int, input().split()))

# 추천받은 기록 저장하기
students = {}

def update_time():
    for student in students:
        students[student] = (students[student][0], students[student][1] + 1)

def find_min_recommend():
    result = []
    min_recommend = int(1e9)
    for student in students:
        min_recommend = min(min_recommend, students[student][0])
    for student in students:
        if min_recommend == students[student][0]:
            result.append(student)

    return result

for recommend in recommends:
    if recommend in gallery:
        students[recommend] = (students[recommend][0] + 1, students[recommend][1])
        continue

    if len(gallery) < N:
        gallery.append(recommend)

        if recommend not in students:
            students[recommend] = (1, 1) # 추천받은 횟수, 시간
        else:
            students[recommend] = (students[recommend][0] + 1, students[recommend][1])

    else: # 비어있는 사진틀이 없는 경우
        min_temp_student = []
        for student in find_min_recommend():
            if student in gallery:
                min_temp_student.append(student)

        if len(min_temp_student) == 1:
            gallery.remove(min_temp_student[0])
            students.pop(min_temp_student[0])

        elif len(min_temp_student) > 1:
            max_time = 0
            old_student = 0
            for student in min_temp_student:
                if max_time < students[student][1]:
                    max_time = students[student][1]
                    old_student = student
            gallery.remove(old_student)
            students.pop(old_student)

        if recommend not in gallery:
            gallery.append(recommend)

        if recommend not in students:
            students[recommend] = (1, 1) # 추천받은 횟수, 시간
        else:
            students[recommend] = (students[recommend][0] + 1, students[recommend][1])

    update_time()

for student in sorted(gallery):
    print(student, end=' ')