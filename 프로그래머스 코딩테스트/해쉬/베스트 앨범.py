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

        for uid in genre_uid_list[:2]:
            answer.append(uid)

    return answer

def solution(genres, plays):
    answer = []

    info = {}
    gens = {}

    for idx, (gen, play) in enumerate(zip(genres, plays)):
        if gen not in info:
            info[gen] = [(idx, play)]
        else:
            info[gen].append((idx, play))

        gens[gen] = gens.get(gen, 0) + play

    for (gen, _) in sorted(gens.items(), key=lambda x:x[1], reverse = True):
        for (idx, _) in sorted(info[gen], key=lambda x:x[1], reverse= True)[:2]:
            answer.append(idx)

    return answer