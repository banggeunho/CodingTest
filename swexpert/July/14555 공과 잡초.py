for tc in range(1, int(input())+1):
    arr = input()
    answer = 0
    for i in range(len(arr)-1):
        temp = arr[i] + arr[i+1]
        
        if temp == '(|' or temp == '|)' or temp == '()':
            answer += 1
	
    print(f'#{tc} {answer}')
            