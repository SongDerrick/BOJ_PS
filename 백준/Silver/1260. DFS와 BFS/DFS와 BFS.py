# 1260 DFS BFS

from collections import deque

N, M, V = map(int, input().split(" "))
# N : 정점 M : 간선 V : 시작 정점의 번호

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
  A, B = map(int, input().split(" "))
  # 간선이 연결하는 두 정점 A,B
  graph[A].append(B)
  graph[B].append(A)

for i in range(1,N+1):
  graph[i].sort()

#print(graph)
dfsresult = []
bfsresult = []


def dfs(graph, visited, start):
  if visited[start] == False:
    visited[start] = True
    dfsresult.append(start)

    for i in graph[start]:
      if not visited[i]:
        dfs(graph, visited, i)


def bfs(graph, visited, start):
  q = deque([start])
  visited[start] = True

  while q:
    k = q.popleft()
    #print(k)
    bfsresult.append(k)
    for i in graph[k]:
      if not visited[i]:
        q.append(i)
        visited[i] = True


dfs(graph, visited, V)
visited = [False] * (N + 1)
for i in dfsresult:
  print(i, end= " ")
print()
bfs(graph, visited, V)
for i in bfsresult:
  print(i, end=" ")
  