import heapq

def solution(jobs):
    answer = 0
    now = 0
    start = -1
    count = 0
    q = []
    jobs.sort()
    
    while count < len(jobs):
        for i in jobs:
            if start < i[0] <= now:
                heapq.heappush(q, (i[1], i[0]))
                
        if len(q) > 0:
            k = heapq.heappop(q)
            start = now
            now += k[0]
            answer += k[0] + start - k[1]
            count += 1            
            
            
            
        else:
            now += 1
        
        
        
        
        
        
    return answer//len(jobs)