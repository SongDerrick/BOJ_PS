def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1 = 0
    s2 = 0
    s3 = 0
    
    
    for idx, i in enumerate(answers):
        if i == supo1[idx%len(supo1)]:
            s1 += 1
        
        if i == supo2[idx%len(supo2)]:
            s2 += 1
            
        if i == supo3[idx%len(supo3)]:
            s3 += 1
            
    print(s1, s2, s3)
    
    m = max(s1, s2, s3)
    for idx, i in enumerate([s1, s2, s3]):
        if i == m:
            answer.append(idx+1)
            
    return answer