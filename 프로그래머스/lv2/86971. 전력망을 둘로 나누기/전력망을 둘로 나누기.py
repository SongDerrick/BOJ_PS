from collections import deque

def bfs(graph, visited, start):
    visited[start] = True
    q = deque([start])
    
    while q:
        k = q.popleft()
        
        for i in graph[k]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def solution(n, wires):
    answer = -1
    result = []
    for j in range(1, n):
        temp = []
        for i in range(1, n):
            if i != j:
                temp.append(i)
        wire = []
        
        for i in temp:
            wire.append(wires[i-1])
        
        visited = [False]*(n+1)
        graph = [[] for _ in range(n+1)]
        for i in wire:
            #print(i)
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        #print(graph)
        a = 0
        
        for i in range(1, n+1):
            if not visited[i]:
                bfs(graph, visited, i)
                for j in visited:
                    if j == False:
                        a += 1
                break

        t = a-1
        #print(abs(t - abs(n-t)))
        result.append(abs(t - abs(n-t)))
    #print(result)
    answer = min(result)
    return answer