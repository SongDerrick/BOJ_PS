from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[i] for i in range(n+1)]
    for i in edge:
        ori = i[0]
        dest = i[1]
        graph[ori].append(dest)
        graph[dest].append(ori)
    
    distance = [0]*(n+1)
    q = deque([graph[1]])
    #print(q)
    
    while q:
        temp = list(q.popleft())
        #print(temp)
        bf = temp[0]
        next = temp[1:]
        for i in next:
            if distance[i] == 0:
                distance[i] = distance[bf] + 1
                q.append(graph[i])
            
    distance[1] = 0
    #print(graph)
    #print(distance)
    curMax = max(distance)
    for i in distance:
        if i == curMax:
            answer += 1
    return answer