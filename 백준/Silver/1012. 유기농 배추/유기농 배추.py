# 1012

import sys
sys.setrecursionlimit(2500)

from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        # print(v)
        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i] = True

                
def dfs(y, x):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if visited[y][x] == False and graph[y][x] == 1:
        visited[y][x] = True
        dfs(y-1, x)
        dfs(y, x-1)
        dfs(y+1, x)
        dfs(y, x+1)
        return True
    return False
    
    
final = []
t = int(input())
for _ in range(t):
    
    temp = []


    m, n, k = map(int, input().split(" "))
    for i in range(k):
        x, y = map(int, input().split(" "))
        temp.append([x,y])
                
    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    for i in range(k):
        x = temp[i][0]
        y = temp[i][1]
        graph[y][x] = 1
    
    
    result = 0
    for i in range(n): # y 좌표
        for j in range(m): # x 좌표
            if dfs(i, j) == True:
                result += 1
    final.append(result)
    temp.clear()
    graph.clear()
    visited.clear()
    
for i in final:
    print(i)