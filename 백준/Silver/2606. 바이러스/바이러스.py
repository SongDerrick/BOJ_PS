# 2602 

# 그래프 탐색, BFS, DFS를 이용해보자!

def dfs(graph, v, visited):
    #print(v)
    visited[v] = True
    global result 
    result += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
       


com = int(input())
net = int(input())
graph = [[] for _ in range(com+1)]

for i in range(net):
    idx, tar = map(int, input().split(" "))
    graph[idx].append(tar)
    graph[tar].append(idx)
    
# 그래프 다 그려 놨다!! 인접 행렬이 아니라 인접 리스트 방식으로 구현했다
# edge에 weight가 없으므로 이런식으로 구현해도 무방!
# DFS로 한번 풀어보자!

result = 0
visited = [False] * (com+1)


dfs(graph, 1, visited)
print(result-1)
            
