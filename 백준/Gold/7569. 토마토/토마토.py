# 7569 토마토
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

M, N, H = map(int, input().split(" "))
graph = []
temp = []
tomato = []
# M은 가로 칸, N은 새로 칸, H는 높이

for z in range(H):
  for y in range(N):
    temp2 = list(map(int, input().split(" ")))
    for i in range(M):
      if temp2[i] == 0:
        temp2[i] = -2
      elif temp2[i] == 1:
        temp2[i] = 0
        tomato.append([i,y,z])
    temp.append(temp2)
  graph.append(temp)
  temp = []
  
#print(graph)
#print(tomato)

def bfs(x,y,z):
  q = deque([[x,y,z]])
  graph[z][y][x] = 0

  while q:
    x1, y1, z1 = q.popleft()
   # print(x1, y1, z1)

    for i in range(6):
      nx = x1 + dx[i]
      ny = y1 + dy[i]
      nz = z1 + dz[i]

      if nx < 0 or ny < 0 or nz < 0 or nx > M-1 or ny > N-1 or nz > H-1:
        continue

      if graph[nz][ny][nx] == -1:
        continue
        
        
      if graph[nz][ny][nx] < 0 or graph[z1][y1][x1] + 1 < graph[nz][ny][nx]:
        graph[nz][ny][nx] = graph[z1][y1][x1] + 1
        q.append([nx, ny, nz])
        

# z, y, x 순서대로 좌표.. ㄷㄷ 

for x,y,z, in tomato:
  #print(x,y,z)
  bfs(x,y,z)

#print(graph)
curMax = 0
final = 0


for z in range(H):
  for y in range(N):
    if -2 in graph[z][y]:
      final = -1
    else:
      curMax = max(curMax, max(graph[z][y]))

if final == -1:
  print(-1)
else:
  print(curMax)