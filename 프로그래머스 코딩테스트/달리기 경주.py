# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    answer = []
    rank_player = {}
    player_rank = {}

    # 랭킹 부여
    for i in range(1, len(players) + 1):
        rank_player[i] = players[i - 1]
        player_rank[players[i - 1]] = i

    # 순위 정하기
    for calling in callings:
        rank = player_rank[calling]

        # 앞 사람
        player_rank[rank_player[rank - 1]] += 1
        player_rank[calling] -= 1

        rank_player[rank - 1], rank_player[rank] = rank_player[rank], rank_player[rank - 1]

    return list(rank_player.values())