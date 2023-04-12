def solution(survey, choices):
    
    result = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0,
    }
    
    for i in range(len(survey)):
        print(survey[i], choices[i])
        if choices[i] < 4:
            if choices[i] == 3:
                result[survey[i][0]] += 1
            elif choices[i] == 2:
                result[survey[i][0]] += 2
            else:
                result[survey[i][0]] += 3
            
        elif choices[i] > 4:
            result[survey[i][1]] += choices[i] - 4
        
    print(result)
    answer = ''
    
    if result['R'] >= result['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if result['C'] >= result['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if result['J'] >= result['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if result['A'] >= result['N']:
        answer += 'A'
    else:
        answer += 'N'
        
        
   
    return answer