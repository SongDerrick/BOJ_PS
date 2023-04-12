from collections import deque

def solution(queue1, queue2):
    total = (sum(queue1) + sum(queue2))
    target = total // 2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    count1 = 0
    count2 = 0
    if total % 2 == 1 or max(q1) > target or max(q2) > target:
        answer = -1
    else:
        t = len(q1)*2
        c1 = sum(q1)
        c2 = sum(q2)
        removed = 0
        while count1 + count2 <=2*t:
            #print(count1, count2)
            
            s1 = c1 - removed
            s2 = c2 + removed
            #print(s1, s2)
            
            if s1 == s2 or not q1 or not q2:
                break
            elif s1 > s2:
                temp = q1.popleft()
                q2.append(temp)
                removed += temp
                count1 += 1
            else:
                temp = q2.popleft()
                q1.append(temp)
                removed -= temp
                count2 += 1 
    
        if s1 != s2:
            answer = -1
        else:
            answer = count1 + count2
    return answer