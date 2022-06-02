def solution(id_list, report, k):
    answer = []
    reported_list = dict()
    reported_cnt = dict()
    mail_list = dict()
    
    for i in id_list:
        reported_cnt[i] = 0
        reported_list[i] = []
        mail_list[i] = 0
        
    for i in report:
        if i.split()[0] not in reported_list[i.split()[1]]:
            reported_list[i.split()[1]].append(i.split()[0])
            reported_cnt[i.split()[1]] += 1
    
    for i in id_list:
        if reported_cnt[i] >= k:
            for j in reported_list[i]:
                mail_list[j] += 1
                
    for i in id_list:
        answer.append(mail_list[i])
        
    return answer