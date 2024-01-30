def solution(n,a,b):
    answer = 1

    # if abs(b - a) != 1:
    #     while abs(b - a) > 1:
    #         a =  (a + 1) // 2
    #         b = (b + 1) // 2
    #         answer += 1
    #     if max(a, b) % 2 == 1:
    #         answer += 1
    
    while True:
        if abs(b - a) == 1 and max(a, b) % 2 == 0:
            break
            
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1
                
        

    return answer

