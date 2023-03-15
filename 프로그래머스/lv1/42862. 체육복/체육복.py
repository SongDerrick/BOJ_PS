def solution(n, lost, reserve):
    students = [0]
    for i in range(n):
        students.append(1)
    
    for i in lost:
        students[i] -= 1
        
    for i in reserve:
        students[i] += 1
        
    
    for i in range(1, n+1):
        if students[i] == 2:
            if i-1 != 0 and students[i-1] == 0:
                students[i-1] += 1
            elif i+1 != n+1 and students[i+1] == 0:
                students[i+1] += 1

    answer = 0
    
    for i in range(1, n+1):
        if students[i] != 0:
            answer += 1
    
    return answer