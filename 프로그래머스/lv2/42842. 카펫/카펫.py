def solution(brown, yellow):
    answer = []
    
    out = brown
    inside = yellow
        
    for i in range(1, out//2):
        v = i
        h = out//2 - i
        
        if v == h:
            break
        
        inner = v * (h-2)
        
        if inner == inside:
            answer.append(h)
            answer.append(v+2)
            break
    return answer