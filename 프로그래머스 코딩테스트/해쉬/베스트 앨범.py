# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    genre_uid = {}
    uid_play = {}
    genre_play = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_uid:
            genre_uid[genre] = [idx]
        else:
            genre_uid[genre].append(idx)
        uid_play[idx] = play
        genre_play[genre] = genre_play.get(genre, 0) + play

    # print(genre_uid)
    # print(uid_play)
    # print(genre_play)

    genre_play_list = list(genre_play)
    genre_play_list.sort(key=lambda x: -genre_play[x])

    for genre in genre_play_list:
        genre_uid_list = list(genre_uid[genre])
        genre_uid_list.sort(key=lambda x: [-uid_play[x], x])
        count = 0
        for uid in genre_uid_list:
            answer.append(uid)
            count += 1
            if count == 2:
                break

    return answer

