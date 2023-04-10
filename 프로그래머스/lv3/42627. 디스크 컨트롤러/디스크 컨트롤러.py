import heapq

def solution(jobs):
    q = []
    answer = 0
    heapq.heapify(jobs)
    print(jobs)
    
    return answer