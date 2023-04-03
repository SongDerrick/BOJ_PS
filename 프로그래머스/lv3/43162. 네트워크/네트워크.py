from collections import deque

def dfs(graph, visited, start):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i-1]:
            dfs(graph, visited, i-1)

def solution(n, computers):
    answer = 0
    noCom = len(computers)
    graph = [[] for _ in range(noCom)]
    visited = [False]*noCom
    #print(graph)
    
    for i in range(noCom):
        for j in range(noCom):
            if i == j:
                continue
            else:
                if computers[i][j] == 1:
                    graph[i].append(j+1)
      
    for i in range(noCom):
        if visited[i] == False:
            dfs(graph, visited, i)
            answer += 1

    #print(graph)
    #print(visited)
    
    return answer