def solution(new_id):
    answer = new_id.lower() # 조건 1
    
    
    for i in answer: # 조건 2
        if i == '-' or i == '_' or i =='.' or 48 <=ord(i) <= 57 or 97 <= ord(i) <= 122:
            continue
        else:
            answer = answer.replace(i,'')
            
    temp = [] # 조건 3
    for i in range(1, len(answer)):
        if answer[i-1] == '.' and answer[i] == '.':
            temp.append(i)
        
    count = 0
    for i in temp:
        i = i - count
        # print(answer[i])
        answer = answer[:i-1] + answer[i:]
        count += 1
            
    if answer and answer[0] == '.': # 조건 4
        answer = answer[1:]
        
    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    if not answer: # 조건 5
        answer = 'a'
        
    if len(answer) >= 16: # 조건 6
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    if len(answer) <= 2:
        #print(answer)
        while True:
            answer += answer[-1]
            
            if len(answer) == 3:
                break

            
            
            
    return answer