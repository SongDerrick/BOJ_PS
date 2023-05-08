# 16928 뱀과 사다리 게임

from collections import deque

N, M = map(int,input().split(" "))

snake = [[] for _ in range(101)]
ladder = [[] for _ in range(101)]
graph = [-1]*101


for _ in range(N):
  depart, arr =  map(int,input().split(" "))
  ladder[depart].append(arr)

for _ in range(M):
  depart, arr =  map(int,input().split(" "))
  snake[depart].append(arr)

def bfs(graph, start):
  graph[start] = 0
  q = deque([start])

  while q:
    curr = q.popleft()
    #print(curr)

    for i in range(1,7):
      if curr + i > 100 or curr + i < 0:
        continue

      
      if snake[curr+i]:
        if graph[snake[curr+i][0]] == -1 or graph[snake[curr+i][0]] > graph[curr] + 1:
          graph[snake[curr+i][0]] = graph[curr] + 1
          q.append(snake[curr+i][0])
        
        
      elif ladder[curr+i]:
        if graph[ladder[curr+i][0]] == -1 or graph[ladder[curr+i][0]] > graph[curr] + 1:
          graph[ladder[curr+i][0]] = graph[curr] + 1
          q.append(ladder[curr+i][0])

        
      elif graph[curr + i] == -1 or graph[curr+i] > graph[curr] + 1:
        graph[curr + i] = graph[curr] + 1
        q.append(curr+i)

        

bfs(graph, 1)
#print(graph)
print(graph[100])

  