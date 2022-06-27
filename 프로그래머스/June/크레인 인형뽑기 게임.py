def solution(board, moves):
    answer = 0
    bucket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0: # 위에서부터 차근차근 검색 인형이 발견될 경우
                if bucket: # 바구니에 인형이 들어있는 경우
                    if bucket[-1] != board[i][move-1]: # 똑같은 인형이 아니면 바구니에 넣기
                        bucket.append(board[i][move-1])
                    else: # 똑같은 인형이 있으면 터뜨리기
                            bucket.pop(-1)
                            answer += 2
                else: # 바구니에 인형이 없는 경우
                    bucket.append(board[i][move-1])
                
                # 크레인으로 꺼낸 인형은 빈 공간으로 바꿔준다.
                board[i][move-1] = 0
                break
            
    return answer