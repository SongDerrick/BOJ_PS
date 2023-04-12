from collections import deque

def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) // 2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    count1 = 0
    count2 = 0
    if max(q1) > target or max(q2) > target:
        answer = -1
    else:
        while count1 != target or count2 != target:
            print(count1, count2)
            s1 = sum(q1)
            s2 = sum(q2)
            if s1 == s2:
                break
            elif s1 > s2:
                q2.append(q1.popleft())
                count1 += 1
            else:
                q1.append(q2.popleft())
                count2 += 1 
    
        if count1 == target or count2 == target:
            answer = -1
        else:
            answer = count1 + count2
    return answer