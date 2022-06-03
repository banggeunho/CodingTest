def solution(lottos, win_nums):
    answer = []
    
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    cnt,zero_cnt = 0, 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
        if i == 0:
            zero_cnt += 1
    
    answer.append(rank[cnt+zero_cnt])
    answer.append(rank[cnt])
    
            
    return answer