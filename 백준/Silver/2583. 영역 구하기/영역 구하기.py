# 2583 영역구하기

from collections import deque

M, N, K = map(int, input().split(" "))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [[0]*N for _ in range(M)]

for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split(" "))
  for j in range(M - y2, M - y1):
    for i in range(x1, x2):
      graph[j][i] = -1

def bfs(x,y):

  count = 1
  graph[y][x] = -1
  q = deque([[x,y]])

  while q:
    x1, y1 = q.popleft()
    #print(x1, y1)
    
    for i in range(4):
      nx = x1 + dx[i]
      ny = y1 + dy[i]

      if nx < 0 or ny < 0 or ny > M-1 or nx > N-1:
        continue
    
      if graph[ny][nx] == -1:
        continue
    
      if graph[ny][nx] >= 0:
        graph[ny][nx] = -1
        q.append([nx, ny])
        count += 1


  return count

#print(bfs(0,4))

t = 0
result = []

for i in range(M):
  for j in range(N):
    if graph[i][j] == 0:
      t += 1
      result.append(bfs(j,i))

print(t)
result.sort()
for i in result:
  print(i, end=" ")


    