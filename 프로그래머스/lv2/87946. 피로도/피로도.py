import itertools

def solution(k, dungeons):
    answer = -1
    d = len(dungeons)
    poss = list(itertools.permutations(dungeons,d))
    curMax = 0
    t = k
    for i in poss:
        k = t
        cur = 0
        #print(i)
        for j in i:
            if k >= j[0]:
                k -= j[1]
                cur += 1
            else:
                break
        curMax = max(cur, curMax)
                
    answer = curMax        
    return answer